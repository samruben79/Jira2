import urllib
function response(){
response = urllib.urlopen('https://wordpress.org/plugins/about/readme.txt')
data = response.read()
 
# Write data to file
filename = "test.txt"
file_ = open(filename, 'w')
file_.write(data)
file_.close()  
}
