import fanout_exchange
import direct_exchange
import topic_exchange

if __name__ == '__main__':
    #amqp_fanout = fanout_exchange.fanout_exchange("exchange")
    #amqp_fanout.consumer("a1")

    amqp_direct = direct_exchange.direct_exchange("exchange2")
    amqp_direct.consumer("b12", "key1")

    #    amqp_topic = topic_exchange.topic_exchange("exchange3")
    #    amqp_topic.consumer("c12","key1")

    pass
