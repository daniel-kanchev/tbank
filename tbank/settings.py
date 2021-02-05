BOT_NAME = 'tbank'
SPIDER_MODULES = ['tbank.spiders']
NEWSPIDER_MODULE = 'tbank.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'tbank.pipelines.DatabasePipeline': 300,
}
