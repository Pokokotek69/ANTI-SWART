loopCount = 0
while True:
    if args.mode == 'both' or args.mode == 'publish':
        message = {}
#        message['message'] = args.message
#        message['sequence'] = loopCount
	f = open("/home/pi/Desktop/python2txtTEST.txt", "r")
        a = f.read()
        messageJson = json.dumps(a)
        myAWSIoTMQTTClient.publish(topic, messageJson, 1)
        if a == 'test':
            print('Published topic %s: %s\n' % (topic, messageJson))
        #loopCount += 1
	break
    time.sleep(1)