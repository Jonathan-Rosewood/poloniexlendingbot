from flask_wtf import Form
from wtforms import StringField, BooleanField, IntegerField, FloatField, DateField
from wtforms.validators import DataRequired


class BotConfig(Form):
    label = StringField('label', validators=[DataRequired()])
    sleeptimeactive = IntegerField('sleeptimeactive', validators=[DataRequired()])
    sleeptimeinactive = IntegerField('sleeptimeinactive', validators=[DataRequired()])
    timeout = IntegerField('timeout', validators=[DataRequired()])
    mindailyrate = IntegerField('mindailyrate', validators=[DataRequired()])
    maxdailyrate = IntegerField('maxdailyrate', validators=[DataRequired()])
    spreadlend = IntegerField('spreadlend', validators=[DataRequired()])
    gapmode = StringField('gapmode')
    gapbottom = IntegerField('gapbottom', validators=[DataRequired()])
    gaptop = IntegerField('gaptop', validators=[DataRequired()])
    xdaythreshold = IntegerField('xdaythreshold', validators=[DataRequired()])
    xdays = IntegerField('xdays', validators=[DataRequired()])
    xdayspread = IntegerField('xdayspread', validators=[DataRequired()])
    transferableCurrencies = StringField('transferableCurrencies')
    minloansize = IntegerField('minloansize', validators=[DataRequired()])
    keepstuckorders = BooleanField('keepstuckorders')
    hidecoins = BooleanField('hidecoins')
    endDate = DateField(format='%Y,%m,%d', validators=[DataRequired()])
    maxtolend = IntegerField('maxtolend', validators=[DataRequired()])
    maxpercenttolend = IntegerField('maxpercenttolend', validators=[DataRequired()])
    maxtolendrate = IntegerField('maxtolendrate', validators=[DataRequired()])
    jsonfile = StringField('jsonfile')
    jsonlogsize = IntegerField('jsonlogsize', validators=[DataRequired()])
    startwebserver = BooleanField('startWebServer')
    customwebserveraddress = StringField('customWebServerAddress')
    customwebserverport = IntegerField('customWebServerPort', validators=[DataRequired()])
    customwebservertemplate = StringField('customWebServerTemplate')
    outputcurrency = StringField('outputCurrency')
    plugins = StringField('plugins')
