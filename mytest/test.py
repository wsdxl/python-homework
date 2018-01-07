"""Train tickets query via command-line.

Usage:
   tickets [-gdtkz] <from> <to> <date>

Options:
   -h,--help   显示帮助菜单
   -g          高铁
   -d          动车
   -t           特快
   -k          快速
   -z          直达

Example:
   tickets 上海 北京 2017-12-05
"""
from docopt import docopt
import requests
from stations import stations
from prettytable import PrettyTable

def cli():
   """command-line interface"""
   arguments = docopt(__doc__)
   print(arguments['<date>'],arguments['<from>'],arguments['<to>'])
   date = arguments['<date>']
   fromstation = stations.get(arguments['<from>'])
   tostation = stations.get(arguments['<to>'])
   url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,fromstation,tostation)
   r = requests.get(url)
#    print(url)
   data=r.json()
   rows=data['data']['result']
   print(rows)
if __name__ == '__main__':
   cli()

# class TrainCollection(object):
#     # 显示车次、出发/到达站、 出发/到达时间、历时、一等坐、二等坐、软卧、硬卧、硬座
#     header = 'train station time duration first second softsleep hardsleep hardsit'.split()
#     def __init__(self, rows):
#         self.rows = rows
#     def _get_duration(self,row):
#         """
#         获取车次运行时间
#         """
#         duration = row.get('lishi').replace(':', 'h') + 'm'
#         if duration.startswith('00'):
#             return duration[4:]
#         if duration.startswith('0'):
#             return duration[1:]
#         return duration

#     @property
#     def trains(self):
#         for row in self.rows:
#             train = [
#                 # 车次
#                 row['station_train_code'],
#                 # 出发、到达站
#            '\n'.join([row['from_staion_name'], row['to_station_name']]),
#                 # 出发、到达时间
#                 '\n'.join([row['start_time'], row['arrive']]),
#                 # 历时
#                 self._get_duration(row),
#                 # 一等坐
#                 row['zy_num'],
#                 # 二等坐
#                 row['ze_num'],
#                 # 软卧
#                 row['rw_num'],
#                 # 软坐
#                 row['yw_num'],
#                 # 硬坐
#                 row['yz_num']
#             ]
#             yield train

#     def pretty_print(self):
#         """
#         数据已经获取到了，剩下的就是提取我们要的信息并将它显示出来。
#         `prettytable`这个库可以让我们它像MySQL数据库那样格式化显示数据。
#         """
#         pt = PrettyTable()
#         # 设置每一列的标题
#         pt._set_field_names(self.header)
#         for train in self.trains:
#             pt.add_row(train)
#         print(pt)
    
#     def cli():
#         """command-line interface"""
#         arguments = docopt(__doc__)
#         print(arguments['<date>'],arguments['<from>'],arguments['<to>'])
#         date = arguments['<date>']
#         fromstation = stations.get(arguments['<from>'])
#         tostation = stations.get(arguments['<to>'])
#         url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,fromstation,tostation)
#         r = requests.get(url)
#         #    print(url)
#         data=r.json()
#         rows=data['data']['result']
#         trains1 = TrainCollection(rows)
#         trains1.pretty_print()
#         if __name__ == '__main__':
#             cli()
        
   

   
   