
from dateutil.parser import parse as du_parse
from dateutil.relativedelta import relativedelta
from datetime import date



def date_tog():
  date1 = 20210524
  s = date.today()
  s = str(s)
  chars = '-'
  date2 = s.translate(str.maketrans('', '', chars))

  d1 = du_parse(str(date1))
  d2 = du_parse(str(date2))
  delta = relativedelta(d2, d1)

  month = 'месяц'
  year = 'год'
  day = 'день'

  dmy = {'y': delta.years, 'm': delta.months, 'd': delta.days}
  words = {
      'y': ['лет', 'год', 'года'],
      'm': ['месяцев', 'месяц', 'месяца'],
      'd': ['дней', 'день', 'дня']
    }

  out = []
  for k, v in dmy.items():
      remainder = v % 10
      if v == 0 or remainder == 0 or remainder >= 5 or v in range(11, 19):
        st = str(v), words[k][0]
      elif remainder == 1:
        st = str(v), words[k][1]
      else:
        st = str(v), words[k][2]
      out.append(" ".join(st))
  return out
