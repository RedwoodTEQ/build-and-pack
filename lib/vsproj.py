import xml.etree.ElementTree as ET
from enum import Enum, auto


def get_csproj_version(csproj_path):
    et = ET.parse(csproj_path)
    root = et.getroot()

    # for child in root:
    #     print(child.tag, child.attrib)
    tag = root.find('PropertyGroup/Version')
    tag.text = tag.text+'_modified'
    print(f'tag text: {tag.text}')

    return root.findtext('PropertyGroup/Version')
    # for type_tag in root.findall('PropertyGroup/Version'):
    #     print(type_tag.text)


def update_version_revision(version_text):
    result = '0.1.0.0'

    if version_text:
        version_numbers = version_text.split(".")

        # if the revision number is missing, append it
        while len(version_numbers) < 4:
            version_numbers.append('0')

        # get revision number and a possible postfix (starts with '-')
        revision_number_text = version_numbers[-1]
        postfix_text = ''
        postfix_position = revision_number_text.find('-')
        if postfix_position > 0:
            postfix_text = revision_number_text[postfix_position:]
            revision_number_text = revision_number_text[0:postfix_position]

        # update version number
        version_numbers[-1] = str(int(revision_number_text) + 1) + postfix_text
        result = '.'.join(version_numbers)
    return result


def get_updated_csproj_version(csproj_path):
    try:
        et = ET.parse(csproj_path)
        version_tag = et.getroot().find('PropertyGroup/Version')
        version_tag.text = update_version_revision(version_tag.text)
        print(f'version_tag.text = {version_tag.text}')

        et.write(r'c:\_temp\et_output.xml')
    except ValueError:
        print('Exception: ValueError')
