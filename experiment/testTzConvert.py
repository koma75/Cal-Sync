import urllib.request
import xml.etree.ElementTree as ET

winzones_url = 'https://raw.githubusercontent.com/unicode-org/cldr/main/common/supplemental/windowsZones.xml'
winzones_xml = urllib.request.urlopen(winzones_url).read().decode()

def timezone_win2iana(tzname, winzones_xml):
    """Convert a Windows timezone name to IANA timezone name

    For example: Central Standard Time -> CST?
    """
    winzones = ET.fromstring(winzones_xml)
    for zone in winzones.findall('.//mapZone'):
        if zone.attrib['territory'] == '001' and zone.attrib['other'] == tzname:
            return zone.attrib['type']
    raise Exception(
        f"Could not find a Windows timezone for a Python timezone named '{tzname}'")

try:
    print(timezone_win2iana("Eastern Standard Time", winzones_xml))
except Exception as e:
    print(e)

def timezone_iana2win(tzname, winzones_xml):
    """Convert a IANA timezone name to a Windows timezone name

    For example: CST -> Central Standard Time
    """
    winzones = ET.fromstring(winzones_xml)
    for zone in winzones.findall('.//mapZone'):
        if zone.attrib['territory'] == '001' and zone.attrib['type'] == tzname:
            return zone.attrib['other']
    raise Exception(
        f"Could not find a Windows timezone for a Python timezone named '{tzname}'")

try:
    print(timezone_iana2win("Asia/Tokyo", winzones_xml))
except Exception as e:
    print(e)

#.Net 6 が標準になればpythonnet でMicrosoft謹製のタイムゾーンID変換IFが使える
# 現状はpythonnetでは.Net 4.0系が参照されてしまうため面倒（自分でバージョン指定すれば可能？未検証
#from clr_loader import get_coreclr
#from pythonnet import set_runtime
#set_runtime(get_coreclr("pythonnetconfig.json")) # これで.NETのバージョン指定ができる？

#{
#  "runtimeOptions": {
#    "tfm": "net6.0",
#    "rollForward": "Minor", // これで指定以降Minorまでは新しい物を参照する
#    "framework": {
#      "name": "Microsoft.NETCore.App",
#      "version": "6.0.0-rc.1.21430.1"
#    }
#  }
#}
#import clr
#
#clr.AddReference('System')
#import System
#
#outStr = ""
#tz = System.TimeZoneInfo
#print(dir(tz))
#
#Result = System.TimeZoneInfo.TryConvertWindowsIdToIanaId("Tokyo Standard Time", outStr)
#
#print(Result)
#print(outStr)
