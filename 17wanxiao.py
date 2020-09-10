import time
import datetime
import json
import requests

check_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"

jsons = {
	"businessType": "epmpics",
	"method": "submitUpInfoSchool",
	"jsonData": {
		"deptStr": {
			"deptid": 71881,
			"text": "信息科学与工程学院-计算机科学与技术(*)-计科F1705"
		},
		"areaStr": "{\"streetNumber\":\"\",\"street\":\"\",\"district\":\"中原区\",\"city\":\"郑州市\",\"province\":\"河南省\",\"town\":\"\",\"pois\":\"河南工业大学(莲花街校区)学生公寓C区-3座\",\"lng\":113.56038400000175,\"lat\":34.83966696227574,\"address\":\"中原区河南工业大学(莲花街校区)学生公寓C区-3座\",\"text\":\"河南省-郑州市\",\"code\":\"\"}",
		"reportdate": 1599714391463,
		"customerid": 43,
		"deptid": 71881,
		"source": "app",
		"templateid": "clockSign2",
		"stuNo": "201716010505",
		"username": "化帅磊",
		"userid": 6615274,
		"updatainfo": [{
			"propertyname": "temperature",
			"value": "36.1"
		}, {
			"propertyname": "symptom",
			"value": "无症状"
		}],
		"customerAppTypeRuleId": 147,
		"clockState": 0
	},
	"token": "adae2729-ab94-4cd6-88fb-4d3d92993738"
}

nowhour = datetime.datetime.now().hour
if nowhour > 21:
	jsons["jsonData"]["customerAppTypeRuleId"] = 146
elif nowhour > 12:
	jsons["jsonData"]["customerAppTypeRuleId"] = 148

response = requests.post(check_url, json=jsons)

res = json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False)
print(res) 
