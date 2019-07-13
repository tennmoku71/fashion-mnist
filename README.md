# tensorflow servingのインストール

https://developers.freee.co.jp/entry/serve-ml-model-by-tensorflow-serving


# dockerの起動

```
docker run -p 8500:8500 -p 8501:8501 -v `pwd`/models:/work -e MODEL_NAME=fmnist_model -e MODEL_BASE_PATH=/work -t tensorflow/serving
```



# curlでテスト

```
python generate_tf_data_file.py

curl -X POST -H "Content-Type: application/json" http://localhost:8501/v1/models/fmnist_model:predict -d @test_data.json

```


# rubyでテスト
```
ruby test.rb
```
