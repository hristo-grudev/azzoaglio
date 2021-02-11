BOT_NAME = 'azzoaglio'

SPIDER_MODULES = ['azzoaglio.spiders']
NEWSPIDER_MODULE = 'azzoaglio.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
	'azzoaglio.pipelines.AzzoaglioPipeline': 100,

}