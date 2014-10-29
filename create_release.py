__author__ = 'Arkady.Babaev'

import os, shutil
from win32api import GetFileVersionInfo, LOWORD, HIWORD
import sys

sourcesdir = "master"
projectpath = "YourProjectDirectoryName" #from sourcedir
projectname = "ProjectName" #as executable name
projectURL = "URL"
companyName = "Dancing Mouse, Inc"
appid_guid = "E58C6728-DC3E-47D4-AC37-4DD82E7031C7" #have to be created once for all time
pathtoicon = "C:\\plug.ico"

####################################################
# FUNCTIONS

def get_version_number (filename):
    try:
        info = GetFileVersionInfo (filename, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)
    except:
        return 0,0,0,0

def ChangeSetting(setname, setvalue, lines):
    for idx, item in enumerate(lines):
        if setname in item:
            tmp_strs =  item.split("=")
            tmp_strs[1] = setvalue+"\n"
            item = '='.join(tmp_strs)
            lines[idx] = item
            return True
    return False

####################################################
# CREATE RELEASE DIRECTORY

if len(sys.argv) <= 1:
    sys.exit()

exepath = os.path.dirname(os.path.realpath(__file__)) + '\\' + sourcesdir + '\\' + projectpath + '\\' + sys.argv[1] + '\\' + projectname + '.exe'
dirname = 'releases\\' + sys.argv[1].lower() + '_' + ".".join([str(i) for i in get_version_number(exepath)])

if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + '\\' + dirname):
    os.makedirs(os.path.dirname(os.path.realpath(__file__)) + '\\' + dirname)

print(os.path.dirname(os.path.realpath(__file__)))

shutil.copy2(exepath, os.path.dirname(os.path.realpath(__file__)) + '\\' + dirname)
shutil.copy2(os.path.dirname(os.path.realpath(__file__)) + '\\dependencies\\boost_python-vc110-mt-1_55.dll', os.path.dirname(os.path.realpath(__file__)) + '\\' + dirname)

####################################################
# CREATE SETUP SCRIPT

lines = []
lines.append('#define MyAppName "' + projectname + '"\n')
lines.append('#define MyAppPublisher "' + companyName + '"\n')
lines.append('#define MyAppURL "' + projectURL + '"\n')
lines.append('#define MyAppExeName "' + projectname + '.exe"\n')
lines.append('\n')
lines.append('[Setup]\n')
lines.append('AppId={{' + appid_guid + '}\n')
lines.append('AppName={#MyAppName}\n')
lines.append('AppVersion=' + ".".join([str(i) for i in get_version_number(exepath)]) + '\n')
lines.append('AppPublisher={#MyAppPublisher}\n')
lines.append('AppPublisherURL={#MyAppURL}\n')
lines.append('AppSupportURL={#MyAppURL}\n')
lines.append('AppUpdatesURL={#MyAppURL}\n')
lines.append('DefaultDirName={pf}\{#MyAppName}\n')
lines.append('DefaultGroupName=' + projectname + '\n')
lines.append('AllowNoIcons=yes\n')
lines.append('OutputDir=.\n') #+ dirname + '\n')
lines.append('OutputBaseFilename=setup_' + projectname + '_' + ".".join([str(i) for i in get_version_number(exepath)]) + '\n')
lines.append('SetupIconFile=' + pathtoicon + '\n')
lines.append('Compression=lzma\n')
lines.append('SolidCompression=yes\n')
lines.append('\n')
lines.append('[Languages]\n')
lines.append('Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"\n')
lines.append('\n')
lines.append('[Tasks]\n')
lines.append('Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked\n')
lines.append('\n')
lines.append('[Files]\n')

for file in os.listdir(os.path.dirname(os.path.realpath(__file__)) + "\\" + dirname):
    if file.endswith(".exe") or file.endswith(".dll"):
        lines.append('Source: "' + file + '"; DestDir: "{app}"; Flags: ignoreversion; Components: ' + projectname + '\main\n')
    elif file.endswith(".dat"):
        lines.append('Source: "' + file + '"; DestDir: "{app}"; Flags: ignoreversion; Components: ' + projectname + '\database\n')
    elif file.endswith(".py"):
        lines.append('Source: "' + file + '"; DestDir: "{app}"; Flags: ignoreversion; Components: ' + projectname + '\scripts\n')

lines.append('Source: "..\\..\\dependencies\\vcredist_x86.exe"; DestDir: "{tmp}"; Flags: ignoreversion; Components: ' + projectname + '\\dependencies\n')
lines.append('Source: "..\\..\\dependencies\\python-suds-0.4\\*"; DestDir: "{tmp}\\python-suds-0.4"; Flags: ignoreversion allowunsafefiles recursesubdirs createallsubdirs; Components: Python\\suds\n')
lines.append('\n')
lines.append('[Components]\n')
lines.append('Name: "' + projectname + '"; Description: "' + projectname + '"; Types: full compact custom\n')
lines.append('Name: "' + projectname + '\\main"; Description: "Main"; Types: full compact custom\n')
lines.append('Name: "' + projectname + '\\database"; Description: "Database"; Types: full custom\n')
lines.append('Name: "' + projectname + '\\scripts"; Description: "Scripts"; Types: full compact custom\n')
lines.append('Name: "' + projectname + '\\dependencies"; Description: "Dependencies"; Types: full custom\n')
lines.append('Name: "Python"; Description: "Python"; Types: full custom\n')
lines.append('Name: "Python\\suds"; Description: "Suds library"; Types: full custom\n')
lines.append('\n')
lines.append('[Icons]\n')
lines.append('Name: "{group}\\{#MyAppName}"; Filename: "{app}\\{#MyAppExeName}"\n')
lines.append('Name: "{group}\\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"\n')
lines.append('Name: "{commondesktop}\\{#MyAppName}"; Filename: "{app}\\{#MyAppExeName}"; Tasks: desktopicon\n')
lines.append('\n')
lines.append('[Registry]\n')
lines.append('Root: HKLM; Subkey: "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};C:\\foo"; Check: NeedsAddPath(\'C:\\Python27\')\n')
lines.append('\n')
lines.append('[Code]\n')
lines.append('\n')
lines.append('function NeedsAddPath(Param: string): boolean;\n')
lines.append('var\n')
lines.append('OrigPath: string;\n')
lines.append('  begin\n')
lines.append('  if not RegQueryStringValue(HKEY_LOCAL_MACHINE,\n')
lines.append('    \'SYSTEM\CurrentControlSet\Control\Session Manager\Environment\',\n')
lines.append('    \'Path\', OrigPath)\n')
lines.append('  then begin\n')
lines.append('    Result := True;\n')
lines.append('    exit;\n')
lines.append('  end;\n')
lines.append('  // look for the path with leading and trailing semicolon\n')
lines.append('  // Pos() returns 0 if not found\n')
lines.append('  Result := Pos(\';\' + Param + \';\', \';\' + OrigPath + \';\') = 0;\n')
lines.append('end;\n')
lines.append('\n')
lines.append('[Run]\n')
lines.append('Filename: "{tmp}\\vcredist_x86.exe"; Description: "Installing vcredist_x86"; WorkingDir: "{tmp}"; StatusMsg: "Installing vcredist_x86 ..."; Flags: skipifdoesntexist\n')
lines.append('Filename: "{tmp}\\python-2.7.6.msi"; Description: "Installing Python 2.7.6"; WorkingDir: "{tmp}"; StatusMsg: "Installing Python ..."; Flags: shellexec skipifdoesntexist\n')
lines.append('Filename: "cmd.exe"; Parameters: "/cpython.exe {tmp}\\python-suds-0.4\\setup.py install"; Description: "Installing Suds 0.4"; WorkingDir: "{tmp}\\python-suds-0.4"; StatusMsg: "Installing Suds ..."; Flags: shellexec skipifdoesntexist\n')
lines.append('\n')

fo = open(os.path.dirname(os.path.realpath(__file__)) + "\\" + dirname + "\\setup_" + "_".join([str(i) for i in get_version_number(exepath)]) + ".iss", "w")
fo.seek(0)
for idx, item in enumerate(lines):
    fo.write(item.encode('utf8'))
fo.truncate()
fo.close()

####################################################
# Changes GEN

import wx
import workForm

app = wx.App()
m = workForm.Main(".".join([str(i) for i in get_version_number(exepath)]))
m.Show(True)
app.MainLoop()

db = workForm.dbcontrol()
lines = db.GetLines()

fo = open(os.path.dirname(os.path.realpath(__file__)) + "\\" + dirname + "\\CHANGELOG", "w")
fo.seek(0)
for idx, item in enumerate(lines):
    fo.write(item.encode('utf8'))
fo.truncate()
fo.close()



