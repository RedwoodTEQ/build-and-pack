import xml.etree.ElementTree as ET


def get_project_version():
    root = ET.parse(
        r'e:\rp\outdoor-asset-tracking\github\GeoSensePluse-Server\GeoSensePlus.Server\GeoSensePlus.Server.csproj').getroot()

    # for child in root:
    #     print(child.tag, child.attrib)

    return root.findtext('PropertyGroup/Version')
    # for type_tag in root.findall('PropertyGroup/Version'):
    #     print(type_tag.text)
    # value = type_tag.get('Version')
    # print(value)
