# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import xml.etree.ElementTree as ET
import json

class XmlJsonConverter:
    @staticmethod
    def _elem_to_dict(elem):
        """
        Recursively converts an ElementTree Element to a dictionary.
        This handles attributes and child nodes.
        """
        result = {}
        
        # Attributes
        if elem.attrib:
            for k, v in elem.attrib.items():
                result[f"@{k}"] = v
        
        # Children
        for child in elem:
            child_data = XmlJsonConverter._elem_to_dict(child)
            
            # Handle multiple children with same tag (list)
            if child.tag in result:
                if isinstance(result[child.tag], list):
                    result[child.tag].append(child_data)
                else:
                    result[child.tag] = [result[child.tag], child_data]
            else:
                result[child.tag] = child_data
        
        # Text/Tail (if leaf node or mixed content)
        text = elem.text.strip() if elem.text else ""
        if text:
            if not result:
                # If no attributes or children, just return the text value
                return text
            else:
                # If attributes or children exist, store text in separate key
                result["#text"] = text
                
        return result

    @staticmethod
    def convert(xml_content):
        try:
            root = ET.fromstring(xml_content)
            # Root element handling
            data = {root.tag: XmlJsonConverter._elem_to_dict(root)}
            return json.dumps(data, indent=4)
        except ET.ParseError as e:
            return f"Error parsing XML: {e}"

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
