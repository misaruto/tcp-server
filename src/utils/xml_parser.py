import xml.etree.ElementTree as ET

class CustomXmlParser():
  def __init__(self,xml_data:str) -> None:
    self.elements = ET.fromstring(xml_data)

  def get_elements(self) -> ET.Element:
    return self.elements
  
  def get_element(self,element_name:str) -> ET.Element:
    return self.elements.find(element_name)
  
  def list_elements(self) -> list:
    for element in self.elements:
      print(f"{element.tag}: {element.text}")
  
  def convert_to_dict(self) -> dict:
    return {self.elements.tag: self.__xml_to_dict(self.elements)}

  def __xml_to_dict(self,element)-> dict:
    if len(element) == 0:
      return element.text
    result = {}
    for child in element:
      child_data = self.__xml_to_dict(child)
      if child.tag in result:
        if isinstance(result[child.tag], list):
          result[child.tag].append(child_data)
        else:
          result[child.tag] = [result[child.tag], child_data]
      else:
        result[child.tag] = child_data
    return result