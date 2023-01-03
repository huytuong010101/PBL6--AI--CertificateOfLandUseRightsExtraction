import sys
if "../" not in sys.path:
    sys.path.append("../")

import re
import json
from modules.Base import Base

class InformationExtraction(Base):
    def __init__(self):
        pass

    def inner_left_extract(self, content):
        data = {}
        # Footer process
        regex = r"\n{1}[^\n]+ngày[^\n]+tháng[^\n]+năm"
        footer_matches = list(re.finditer(regex, content))
        if not footer_matches:
            raise Exception("Cannot extract footer")
        footer = content[footer_matches[-1].start():]
        content = content[:footer_matches[-1].start()]
        regex = r"\n[^\n:]+:[^\n]+"
        infors = re.findall(regex, footer)
        for infor in infors:
            key, value = infor.split(":")
            data[key.strip()] = value.strip()
        # Body processing
        regex = r"[1-9]{1}\.[^:\n]+:"
        matches = list(re.finditer(regex, content))
        for i in range(len(matches)):
            # Get section and title
            title = content[matches[i].start(): matches[i].end()]
            section = content[matches[i].end():matches[i+1].start() if i +1 < len(matches) else 10000]
            
            # Extraction infor
            subdata = {}
            regex = r"""[^1234567890\n,.?:"\{\}\+_*&^%$#@!~<>/;'\[\]]+:"""
            submatches = list(re.finditer(regex, section))
            for j in range(len(submatches)):
                infor = section[submatches[j].start():submatches[j+1].start() if j +1 < len(submatches) else 10000]
                key, value = infor.split(":")[0], ":".join(infor.split(":")[1:]) 
                subdata[key.strip()] = value.strip().replace("\n", " ")
            if not subdata or "ghi chú" in title.lower(): # TODO: fix hardcode here
                subdata = section.strip()
            data[title] = subdata
        return data

    def front_extract(self, content):
        data = {}

        regex = r"[I]. [^\n]+"
        match = re.search(regex, content)
        if match is None:
            regex = r". người sử dụng[^\n]+"
            match = re.search(regex, content.lower()) 
        if match is None:
            return data
        content = content[match.end() + 1:]
        content = "\n".join(content.splitlines()[:-1])
        # Get the name if exception
        name = ""
        lines = content.splitlines()
        while ":" not in lines[0]:
            name = name + lines[0]
            del lines[0]
        if name:
            data["Chủ sở hữu"] = name
        # ===
        regex = r"""[^\n,.?:"\{\}\+_\)(*&^%$#@!~<>/;'\[\]]+:"""
        matches = list(re.finditer(regex, content))
        
        for i in range(len(matches)):
            infor = content[matches[i].start(): matches[i+1].start() if i+1 < len(matches) else 10000]
            key, value = infor.split(":")
            data[key.strip()] = value.strip().replace("\n", " ")
        return data

    def __call__(self, 
                 front: str=None, 
                 inner_left: str=None, 
                 inner_right: str=None, 
                 back: str=None,
                 is_debug: bool=False):
        data = {}
        if front is not None:
            try:
                front_data = self.front_extract(front)
                data["Thông tin về chủ sở hữu"] = front_data
            except Exception as e:
                print(front)
                print(e)

        if inner_left is not None:
            try:
                inner_left_data = self.inner_left_extract(inner_left)
                data["Thửa đất, nhà ở và tài sản khác gắn liền với đất"] = inner_left_data
            except Exception as e:
                print(inner_left)
                print(e)

        if is_debug:
            print(json.dumps(data, indent=4, ensure_ascii=False))
        return data