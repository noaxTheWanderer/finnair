import requests

def get_sentiments(texts):
	texts = []
	for index in corpus.keys():
		line = corpus[index]["line"]
		dic = {"body" : line, "id" : str(index)}
		texts.append(dic)
	body = json.dumps({"language":"en", "texts": texts})
	apiKey = "4a30f6a793ed725eb059d475a887a936"
	r = requests.post("https://api.gavagai.se/v3/tonality?apiKey="+apiKey , data = body, headers={"Content-Type":"application/json"})
	gavagai_json = r.json()
	return gavagai_stats(gavagai_json, texts)

def gavagai_stats(gavagai_json, original_texts):
	csv = {}
	texts = gavagai_json["texts"]
	for text in texts:
		index = int(text["id"])
		orig = original_texts[index]
		tonality = text["tonality"]
		csv[org] = {}
		for tone in tonality:
			csv[org][tone["tone"]] = tone["normalizedScore"]
	return csv