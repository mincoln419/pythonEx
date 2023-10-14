import requests


results = []

idx = "PLhzBuObIigYNJGczvJavgQoV6Nm58gqk9"
url="https://www.youtube.com/playlist?list={}".format(idx)
header = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "referer":"https://www.youtube.com"
}

r = requests.get(url, headers = header)

find_text = "var ytInitialData = "
start_index = r.text.find(find_text)
if start_index >= 0:
    end_index = r.text.find("};", start_index)
    if end_index > start_index:
        str_data = r.text[start_index + len(find_text): end_index + 1]
        # print(str_data)
        list_str = str_data.split('playlistVideoRenderer":{')[1:]
        find_1 = ('"videoId":"','",')
        find_2 = ('[{"text":"','"}')
        find_3 = ('"lengthSeconds":"', '",')
        
        for i, t in enumerate(list_str):
            start_index_find_1 = t.find(find_1[0]) + len(find_1[0])
            start_index_find_2 = t.find(find_2[0]) + len(find_2[0])
            start_index_find_3 = t.find(find_3[0]) + len(find_3[0])
            
            end_index_find_1 = t.find(find_1[1], start_index_find_1)
            end_index_find_2 = t.find(find_2[1], start_index_find_2)
            end_index_find_3 = t.find(find_3[1], start_index_find_3)
            
            vid = t[start_index_find_1 : end_index_find_1].replace('"', "").strip()
            title = t[start_index_find_2 : end_index_find_2].replace('"', "").strip()
            length = t[start_index_find_2 : end_index_find_2].replace('"', "").strip()
            
            if length.isnumeric:
                results.append({
                    "vid" : vid,
                    "title" : title,
                    "length" : length,
                    "url" : "https://www.youtube.com/watch?v={}".format(vid)
                })
        print(results)