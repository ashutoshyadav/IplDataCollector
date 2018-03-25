import urllib2
import json
import re

class IPL():

	def __init__(self):
		# self.get_data_2017()
		# self.get_data_2016()
		# self.get_data_2015()
		# self.get_data_2008()
		# self.get_data_2011()
		# self.get_data_2012()
		self.get_data_2014()

	def get_data_2014(self):
		url = 'http://ncrcricket.com/players-sold-in-ipl-7-auction/'
		data = urllib2.urlopen(url).read()
		print len(data)
		# print data
		res = re.findall(r'<tr style="height: 15.75pt;">[\r\n|\r|\n]<td class="xl6620523" style="height: 15.75pt;" height="21">(.*?)</td>[\r\n|\r|\n]<td class="xl6620523">.*?</td>[\r\n|\r|\n]<td class="xl6620523">.*?</td>[\r\n|\r|\n]<td class="xl6520523">(.*?)</td>[\r\n|\r|\n]</tr>',data)
		print len(res)
		f = open('ipl2014.csv','w')
		for row in res:
			print row
			s = ''
			# temp = row[0].split(',')
		# 	# s += str(temp[1])+' '+str(temp[0])+','
			s += str(row[0])+','
			try:
				temp = row[1].split(',')
				for item in temp:
					s+= str(item)
				s += ','
			except:
				s += str(row[1])+','
		# 	s += str(row[1])+','
		# 	s += str(row[2])+'\n'
		# 	# temp = row[2].split(',')
		# 	# for item in temp:
		# 	# 	s += str(item)
			s += '\n'
			f.write(s)
		f.close()

	def get_data_2012(self):
		url = 'http://www.cricketcountry.com/news/list-of-all-players-sold-in-ipl-auction-2012-11058'
		data = urllib2.urlopen(url).read()
		print len(data)
		# print data
		res = re.findall(r'<tr>[\r\n|\r|\n]<td width="150" valign="top">[\r\n|\r|\n]<p>(.*?)</p>[\r\n|\r|\n]</td>[\r\n|\r|\n]<td width="118" valign="top">[\r\n|\r|\n]<p>(.*?)</p>[\r\n|\r|\n]</td>[\r\n|\r|\n]<td width="93" valign="top">[\r\n|\r|\n]<p>(.*?)</p>[\r\n|\r|\n]</td>[\r\n|\r|\n]<td width="85" valign="top">[\r\n|\r|\n]<p>(.*?)</p>[\r\n|\r|\n]</td>[\r\n|\r|\n]<td width="90" valign="top">[\r\n|\r|\n]<p>(.*?)</p>[\r\n|\r|\n]</td>[\r\n|\r|\n]<td width="81" valign="top">[\r\n|\r|\n]<p>(.*?)</p>[\r\n|\r|\n]</td>[\r\n|\r|\n]</tr>',data)
		print len(res)
		f = open('ipl2012.csv','w')
		for row in res:
			print row
			s = ''
			# temp = row[0].split(',')
			# s += str(temp[1])+' '+str(temp[0])+','
			s += str(row[0])+','
			s += str(row[3])+','
			try:
				temp = row[4].split(',')
				for item in temp:
					s+= str(item)
				s += ','
			except:
				s += str(row[4])+','
			try:
				temp = row[5].split(',')
				for item in temp:
					s+= str(item)
				s += '\n'
			except:
				s += str(row[5])+'n'
		# 	# temp = row[2].split(',')
		# 	# for item in temp:
		# 	# 	s += str(item)
		# 	# s += '\n'
			if(row[2]=="Sold"):
				f.write(s)
		# f.close()


	def get_data_2011(self):
		url = 'http://www.espncricinfo.com/indian-premier-league-2011/content/story/495897.html'
		data = urllib2.urlopen(url).read()
		print len(data)
		# print data
		res = re.findall(r'<tr>[\r\n|\r|\n]<td>(.*?)</td>[\r\n|\r|\n]<td>.*?</td>[\r\n|\r|\n]<td>(.*?)</td>[\r\n|\r|\n]<td>(.*?)</td>[\r\n|\r|\n]</tr>',data)
		print len(res)
		f = open('ipl2011.csv','w')
		for row in res:
			print row
			s = ''
			# temp = row[0].split(',')
			# s += str(temp[1])+' '+str(temp[0])+','
			s += str(row[0])+','
			s += str(row[1])+','
			s += str(row[2])+'\n'
			# temp = row[2].split(',')
			# for item in temp:
			# 	s += str(item)
			# s += '\n'
			f.write(s)
		f.close()

	def get_data_2008(self):
		url = 'https://en.wikipedia.org/wiki/2008_Indian_Premier_League'
		data = urllib2.urlopen(url).read()
		res = re.findall(r'<td><span class="sortkey">(.*?)</span><span.*?</span></td>[\r\n|\r|\n]<td><a href=".*?">(.*?)</a></td>[\r\n|\r|\n]<td align="right">(.*?)</td>',data)
		print len(res)
		f = open('ipl2008.csv','w')
		for row in res:
			print row
			s = ''
			temp = row[0].split(',')
			s += str(temp[1])+' '+str(temp[0])+','
			# s += str(row[0])+','
			s += str(row[1])+','
			temp = row[2].split(',')
			for item in temp:
				s += str(item)
			s += '\n'
			f.write(s)
		f.close()
	

	def get_data_2015(self):
		url = 'http://www.espncricinfo.com/indian-premier-league-2015/content/story/832783.html'
		data = urllib2.urlopen(url).read()
		res = re.findall(r'<a href.*?><b>(.*?)</b></a> - (.*?)\n',data)
		print len(res)
		f = open('ipl2015.csv','w')
		for row in res:
			print row
			s = ''
			s += str(row[0])+','
			# s += str(row[1][11:-12])+','
			temp = row[1].split(' - ')
			# print temp
			try:
				s += str(temp[0])+','+str(temp[1])+'\n'
			except:
				s += str(row[2])+'\n'
			f.write(s)
		f.close()
	

	def get_data_2016(self):
		url = 'http://www.espncricinfo.com/indian-premier-league-2016/content/story/969473.html'
		data = urllib2.urlopen(url).read()
		res = re.findall(r'<b><a href.*?>(.*?)(Base price.*?)<b>(.*?)</b>',data)
		print len(res)
		f = open('ipl2016.csv','w')
		for row in res:
			print row
			s = ''
			s += str(row[0][:-10])+','
			s += str(row[1][11:-12])+','
			temp = row[2].split(' for ')
			print temp
			try:
				s += str(temp[0])+','+str(temp[1])+'\n'
			except:
				s += str(row[2])+'\n'
			f.write(s)
		f.close()
		

	def get_data_2017(self):
		url = 'http://www.espncricinfo.com/indian-premier-league-2017/content/story/1083407.html'
		data = urllib2.urlopen(url).read()
		res = re.findall(r'<b><a href.*?>(.*?)(Base price.*?)<b>(.*?)</b>',data)
		print len(res)
		f = open('ipl2017.csv','w')
		for row in res:
			s = ''
			s += str(row[0][:-10])+','
			s += str(row[1][11:-12])+','
			temp = row[2].split(' for ')
			s += str(temp[0])+','+str(temp[1])+'\n'
			f.write(s)
		f.close()
		


if __name__=="__main__":
	IPL()
