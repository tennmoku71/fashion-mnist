require 'net/http'
require 'uri'

uri = URI.parse("http://localhost:8501/v1/models/fmnist_model:predict")
request = Net::HTTP::Post.new(uri)
request.content_type = "application/json"
request.body = ""
request.body << File.read("ruby_data.json").delete("\r\n")

req_options = {
  use_ssl: uri.scheme == "https",
}

response = Net::HTTP.start(uri.hostname, uri.port, req_options) do |http|
  http.request(request)
end

p response.code
p response.body