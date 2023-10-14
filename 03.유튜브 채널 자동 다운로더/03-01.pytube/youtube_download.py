from urllib.request import Request, urlopen
import requests
import json
import pprint
import ffmpeg

def download_url(data, filename):
    if data is None:
        print("Data is None")
        return None
    sample_url = data["url"]
    quality = data["quality"]
    print("동영상 주소 >>>>> ", sample_url, quality)
    request = Request(sample_url, headers=header)
    r = urlopen(request)
    filesize = int(r.headers["Content-Length"])
    print("다운로드 사이즈 >>>>", filesize )
    
    download_size = 0
    block_size = 8129
    with open(filename, "wb") as f:
        while True:
            buffer = r.read(block_size)
            if not buffer:
                break
            download_size += len(buffer)
            f.write(buffer)
            status = "{:10d} [{:03.2f}%]".format(download_size, download_size*100.0 / filesize)
            print(status)
        print(">>> 다운로드 완료 <<<")   
    
def find_list(listdata, key, value):
    for item in listdata:
        if item.get(key) == value:
            return item
    return None

header = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "referer":"https://www.youtube.com"
}

video_id = "o5dUNru_b8I"

url = "https://www.youtube.com/watch?v={}".format(video_id)


watch_html = urlopen(url).read().decode("utf-8")
r = requests.get(url, headers=header)


parse = "ytInitialPlayerResponse = "
start_index = watch_html.find(parse)
end_index = watch_html.find("};", start_index + 1) if start_index >= 0 else 0


# if start_index < end_index:
#     h = watch_html[start_index + len(parse):end_index + 1]
#     _json = json.loads(h)
#     pprint.pprint(_json)
#     with open('output.txt', 'wt', encoding="utf-8") as out:
#         pprint.pprint(_json, stream=out)

if start_index < end_index :
    h = watch_html[start_index + len(parse) : end_index + 1]
    json_data = json.loads(h)

    aformats = json_data["streamingData"]["adaptiveFormats"]
    # for f in aformats:
    #     print("{},{},{},{}".format(f["itag"], f["mimeType"], f["quality"], f["url"][0:30]))
    # print(find_list(aformats, "itag", 243))
    # print([item for item in aformats if item["itag"] == 137])
    video = next((item for item in aformats if item["itag"] == 247), None)
    audio = next((item for item in aformats if item["itag"] == 140), None)
    
    video_filename = "{}_video.mp4".format(video_id)
    audio_filename = "{}_audio.mp4".format(video_id)
    download_url(video,video_filename)
    download_url(audio,audio_filename)
    input_v = ffmpeg.input(video_filename)
    input_a = ffmpeg.input(audio_filename)
    output_filename = "{}_all.mp4".format(video_id)
    ffmpeg.output(input_v, input_a, output_filename, vcodec="copy", acodec="copy").run()
    print(">>>> 작업완료 <<<<")


