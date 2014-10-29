ver_counter
===========
That is small set of scripts to create autoversion counter (and some workaround) for IDE that do not support it by default.
I wrote it for myself some time ago and still use it.

List of achieves:
- it automatically keeps VERSION file in your repository
- it helps to describe your changes after each success rebuild (in small UI, written using wxWidgets) and store them into small project database (sqlite)
- it automatically creates CHANGELOG, using info from database
- it automatically create InnoSetup instructions for project (to create installer)

External dependencies:
- Python
- Python libraries:
	- wx
	- sqlite3


Instructions for Visual Studio
==============================
1) Resource file

First you have to add to your project version resource file.
For VS2013 it is possible to do at: 

> Solution Explorer -> Solution -> Project -> Resource Files -> Add... -> Resource -> Version -> New.

Then in created resource file you have to add at top of file:

> #include "config.h"

Change next lines:

 FILEVERSION VER_FILE_VERSION
 PRODUCTVERSION VER_PRODUCT_VERSION
 FILEFLAGS VER_FILEFLAGS
 FILEOS VER_FILEOS
 FILETYPE VER_FILETYPE

 and inside "BEGIN" "END" change next lines:
 
	VALUE "FileDescription",  VER_FILE_DESCRIPTION_STR "\0"
	VALUE "FileVersion",   VER_FILE_VERSION_STR "\0"
	VALUE "InternalName",  VER_INTERNAL_NAME_STR "\0"
	VALUE "LegalCopyright",   VER_COPYRIGHT_STR "\0"
	VALUE "OriginalFilename", VER_ORIGINAL_FILENAME_STR "\0"
	VALUE "ProductName",   VER_PRODUCTNAME_STR
	VALUE "ProductVersion",   VER_PRODUCT_VERSION_STR "\0"
  
It is created this way, because structure of resource files may be different at different IDE's, that is why it is important to create universal set of rules, and prepare resource file of actual system to use that set.

2) Create/open config.h in your project and add there next lines:

	#define STRINGIZE2(s) #s
	#define STRINGIZE(s) STRINGIZE2(s)

	#define VERSION_MAJOR 0
	#define VERSION_MINOR 1
	#define VERSION_BUILD 0
	#define VERSION_REVISION 0
	 
	#define VER_FILE_DESCRIPTION_STR <MY_FAVORITE_DESCRIPTION>
	#define VER_FILE_VERSION         VERSION_MAJOR, VERSION_MINOR, VERSION_BUILD, VERSION_REVISION
	#define VER_FILE_VERSION_STR     STRINGIZE(VERSION_MAJOR)     \
										"." STRINGIZE(VERSION_MINOR) \
										"." STRINGIZE(VERSION_BUILD) \
										"." STRINGIZE(VERSION_REVISION)
	 
	#define VER_PRODUCTNAME_STR      <NAME OF CREATED EXECUTABLE>
	#define VER_PRODUCT_VERSION      VER_FILE_VERSION
	#define VER_PRODUCT_VERSION_STR  VER_FILE_VERSION_STR
	#define VER_ORIGINAL_FILENAME_STR   VER_PRODUCTNAME_STR ".exe"
	#define VER_INTERNAL_NAME_STR    VER_ORIGINAL_FILENAME_STR
	#define VER_COPYRIGHT_STR        "Copyright (C) 2014"
	 
	#ifdef _DEBUG
	  #define VER_VER_DEBUG          VS_FF_DEBUG
	#else
	  #define VER_VER_DEBUG          0
	#endif

	#define VER_FILEOS               0x40004L
	#define VER_FILEFLAGS            VER_VER_DEBUG
	#define VER_FILETYPE             0x1L

You should change strings embraced by <>.
Maybe also you will need to change some other descriptions and parameters. Just because you want it, or because your operating system, IDE or something else is different then mine.

As example you can take config.h, that goes with that scripts.

Be careful with last line, it has to exist and be empty, that is bug of microsoft resource compiler.

3) Copy BuildIncrement.py to your project folder.
It will read config.h, change there versions and write it back.

4) At Pre-build order for your compiler you have to set 

> python $(ProjectDir)\BuildIncrement.py

So, it will call it every time before building.
You can change it's logic to change sequence of increasing, random for build increment and etc.

You will need to have any installed Python version.

5) Copy create_release.py and PyForm.py to folder that holds your development folders (as 'master'), and will holds folder for releases and etc.

6) Create directories: releases and dependencies at the same level, as your source directory.
Open create_release.py. You will need to customize InnoSetup settings (or simply delete lines about it and don't read rest of 6) ).

At head change:
 - sourcesdir - put your source directory (I guess it will be "trunk" or "master")
 - projectpath - path to your project from sourcesdir.
 - projectname - name of your executable.
 - projectURL
 - companyName
 - appid_guid
 - pathtoicon
 
Beware: at head of create_release we import windows dependency libraries. At another OS you have to change it the way you need it. 
Then find lines starting with:

> shutil.copy2

That will copy all stuff you need from anywhere to release directory. That may be config files, small file databases, libraries and executables that are result of your compilation, or just need to exist at release directory.
Usually, it needs once to input and add something if something has changed.
After lines starting with:

> for file in os.listdir(os.path.dirname(os.path.realpath(__file__)) + "\\" + dirname):

It is possible to split your release at different parts, that user will be able to choose separately.
After them you have to choose dependencies: external software that have to be installed. And set them as needs. There exist some examples. Or just delete lines.

Examples:
> lines.append('Source: "..\\..\\dependencies\\vcredist_x86.exe"; DestDir: "{tmp}"; Flags: ignoreversion; Components: ' + projectname + '\\dependencies\n')
> lines.append('Source: "..\\..\\dependencies\\python-suds-0.4\\*"; DestDir: "{tmp}\\python-suds-0.4"; Flags: ignoreversion allowunsafefiles recursesubdirs createallsubdirs; Components: Python\\suds\n')

After that you may add changes to components.
Then there goes example how to change PATH using InnoSetup. Delete it, use it.

7) At Post-build order of your compiler you have to set:

> python <path to your scripts>\create_release.py Release

for release and 

> python <path to your scripts>create_release.py

for debug. Or just ignore parameter that for Debug.