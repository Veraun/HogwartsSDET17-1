def test_jenkins():
    import jenkins

    server = jenkins.Jenkins('http://127.0.0.1:8086/', username="admin", password="11b6f47797d686d6f723d932facef6e093")

    # 查询当前jenkins下任务个数
    # print(server.jobs_count())

    # 启动jenkins任务
    print(server.build_job("cekai17"))