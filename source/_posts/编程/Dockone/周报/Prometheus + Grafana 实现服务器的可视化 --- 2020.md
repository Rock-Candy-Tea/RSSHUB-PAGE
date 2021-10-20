
---
title: 'Prometheus + Grafana 实现服务器的可视化 --- 2020'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://miro.medium.com/max/1400/1*Gx--pGz8qRUmf86N614LIA.png'
author: Dockone
comments: false
date: 2021-10-20 10:08:41
thumbnail: 'https://miro.medium.com/max/1400/1*Gx--pGz8qRUmf86N614LIA.png'
---

<div>   
<br>Prometheus + Grafana 实现服务器的可视化 --- 2020<br>
<br>设置 Prometheus、Node Exporter 和 Grafana 以获得服务器指标的图形可视化。<br>
<br><img src="https://miro.medium.com/max/1400/1*Gx--pGz8qRUmf86N614LIA.png" alt referrerpolicy="no-referrer"><br>
<br><h3>Prometheus 简介</h3><strong>Prometheus</strong> 是一个开源监控工具，实现了高维数据模型。Prometheus 有多种数据可视化模式，其中一种是集成 Grafana 。Prometheus 以高效的自定义格式将时间序列数据存储在内存和本地磁盘上。<br>
<br>Prometheus 有许多客户端可用于轻松监控服务，也可以轻松创建自定义客户端。每台服务器的可靠性都是独立的，仅依赖本地存储。用 <a href="https://medium.com/javarevisited/7-online-courses-to-learn-golang-or-go-programming-languages-in-2020-f599a25cf14a">golang</a> 编程语言编写，所有二进制文件都是静态链接的，易于部署。<br>
<br>Prometheus 采用拉取策略而不是推送策略，即 prometheus 以一定的时间间隔从 exporter 那里拉取数据，而不是exporter推送数据到prometheus。这种方式有其自身的优点和缺点，但我们不讨论这些细节。<br>
<br><h3>Grafana 简介</h3><strong>Grafana</strong> 是一款开源可视化和分析软件，它允许您查询、可视化、提醒和探索您的指标，无论这些指标存储在哪里。Grafana 支持数十种数据库，我们可以创建一个仪表盘来可视化它们全部。<br>
<br>Grafana 还提供报警，直观地定义阀值，并通过 Slack、 PagerDuty 和其他平台获得通知。Grafana 还提供了多种选项来查看我们的数据，从热力图到直方图，从图形到地理地图。 Grafana 有大量的可视化选项可以帮助我们更好地理解数据。我正在使用 <strong>Ubuntu 18.04</strong>，并将显示与其相关的整个配置。<br>
<br><h3>Prometheus 安装</h3><img src="https://miro.medium.com/max/1400/1*Zp0Xylt66SclidQaJPlb_g.png" alt referrerpolicy="no-referrer"><br>
<br>```<br>
wget <a href="https://github.com/prometheus/prometheus/releases/download/v2.21.0/prometheus-2.21.0.linux-amd64.tar.gz" rel="nofollow" target="_blank">https://github.com/prometheus/ ... ar.gz</a><br>
<br>tar -xzf prometheus-2.21.0.linux-amd64.tar.gz<br>
<br>cd prometheus-2.21.0.linux-amd64/<br>
<br>./prometheus<br>
```<br>
<br>安装非常简单，执行这些命令将会让 Prometheus 服务器在端口 9090 中运行。prometheus 在端口9090上的仪表板如下图所示：<br>
<br><img src="https://miro.medium.com/max/1400/1*YJnRAgTcB4hQnqNX_uU52w.png" alt referrerpolicy="no-referrer"><br>
<br>如前所述，从 prometheus 中抓取的指标发生在恒定的时间段内，因此可以在路径 /metrics 中查看它们<br>
<br><img src="https://miro.medium.com/max/1400/1*kEDlP3ZrstPg9_ENfHeetQ.png" alt referrerpolicy="no-referrer"><br>
<br><img src="https://miro.medium.com/max/1400/1*mmf053jeOPY0MTgNolzTcQ.png" alt="Graph visualization of query in prometheus dashboard" referrerpolicy="no-referrer"><br>
<br>这些指标用于形成具有各种聚合函数的复杂表达式，以我们想要的形式进行可视化，这在promql的帮助下基本上是可能的。prometheus 中的图形可视化非常基本，没有提供太多自定义，因此我们将使用 <strong><em>Grafana</em></strong>。<br>
<br><h3>节点 Exporter 安装</h3><img src="https://miro.medium.com/max/1400/1*DZqn6yIwCsMoi3XNUvZpUg.png" alt referrerpolicy="no-referrer"><br>
<br>```<br>
wget <a href="https://github.com/prometheus/node_exporter/releases/download/v1.0.1/node_exporter-1.0.1.linux-amd64.tar.gz" rel="nofollow" target="_blank">https://github.com/prometheus/ ... ar.gz</a><br>
<br>tar -xzf node_exporter-1.0.1.linux-amd64.tar.gz<br>
<br>cd node_exporter-1.0.1.linux-amd64/<br>
<br>./node_exporter<br>
```<br>
<br>上述命令将安装节点 exporter 并在端口 9100 上运行，并且可以从 /metrics 扩展中抓取指标。<br>
<br>我创建了3个虚拟机并在所有虚拟机中安装了节点 exporter，以提供更好的可视化效果。所以在安装之后，我们必须告诉 prometheus 从哪里抓取指标，这可以通过编辑 prometheus.yml 文件来完成。我们只需要在 scrape_configs 中添加一个新作业，指定目标中的 IP 地址和端口。在 prometheus.yml 文件中添加目标并重新启动 prometheus 服务器后，我们可以在仪表板以及 /targets 路径中看到新目标及其状态。<br>
<br><img src="https://miro.medium.com/max/1400/1*Mi5aZ5MnCZKZPV-VDQlXVQ.png" alt referrerpolicy="no-referrer"><br>
<br><img src="https://miro.medium.com/max/1400/1*UCnAizJvir6lPHT-4DQoGg.png" alt referrerpolicy="no-referrer"><br>
<br>确保所有目标都已启动，如果没有，请检查是否为该 VM 实例开放了 9100 端口。您还可以查看 prometheus 从每个 exporter 抓取的时间以及上次抓取的时间。<br>
<br><h3>Grafana 安装</h3><img src="https://miro.medium.com/max/1400/1*xvJnbuc7c3DE_Tpa0bvW5A.png" alt referrerpolicy="no-referrer"> <br>
<br>```<br>
wget <a href="https://dl.grafana.com/oss/release/grafana-7.1.5.linux-amd64.tar.gz" rel="nofollow" target="_blank">https://dl.grafana.com/oss/rel ... ar.gz</a><br>
<br>tar -xzf grafana-7.1.5.linux-amd64.tar.gz<br>
<br>cd grafana-7.1.5.linux-amd64/<br>
<br>./bin/grafana-server<br>
```<br>
<br>通过运行上述命令即可完成安装，grafana 运行在端口 3000。默认的用户名和密码均为“admin”。<br>
<br>当我们进入仪表板，我们需要添加一个数据源，在我们的例子中是 Prometheus。我们只需要提供 prometheus URL 并点击 保存 和 测试 按钮。如果我们看到一个成功的提示框，说数据源正在工作，那么我们就可以开始了。<br>
<br><img src="https://miro.medium.com/max/1400/1*-aey4e3NacPIsS4HlP-7oA.png" alt referrerpolicy="no-referrer"><br>
<br>我们可以使用自定义的查询语句创建自己的仪表板和面板，但这是一项乏味的工作。因此，为了简化我们的工作，其他用户已经创建了一些仪表板，我们可以使用相同的仪表板并根据我们的需要调整表达式。我使用的是1860和405，这些是我们导入仪表板的唯一ID。<br>
<br><img src="https://miro.medium.com/max/1400/1*LOQKg1_p3zS_JjUqpIPc3A.png" alt referrerpolicy="no-referrer"><br>
<br><img src="https://miro.medium.com/max/1400/1*-9qj0uUOqUlWpSHIqgBo5A.png" alt referrerpolicy="no-referrer"><br>
<br>导入完成后，我们会看到基于其表达式和时间范围的图表。您可以通过将时间范围减少到5分钟来深入了解。<br>
<br><img src="https://miro.medium.com/max/1400/1*TFpk8YC8Be33kxggnvk6rg.png" alt referrerpolicy="no-referrer"><br>
<br><img src="https://miro.medium.com/max/1400/1*OXJfrLvaq8fIwDp1VIP-1Q.png" alt referrerpolicy="no-referrer"><br>
<br><img src="https://miro.medium.com/max/1400/1*aNmR89AoAkCkbzpe1KAZ1A.png" alt referrerpolicy="no-referrer"><br>
<br>Grafana还允许我们查看合并多个 exporter的表单，以便更好地进行比较。<br>
<br><img src="https://miro.medium.com/max/1400/1*SMIcvuIDkpEIuqB8i02Cow.png" alt referrerpolicy="no-referrer"><br>
<br><img src="https://miro.medium.com/max/1400/1*Gx--pGz8qRUmf86N614LIA.png" alt referrerpolicy="no-referrer"><br>
<br>所以在上面的图片中，我们可以看到所有三个节点exporter的数据都被可视化了。<br>
<br>以上总结了 Prometheus 和 Grafana 的基本设置，用来可视化节点指标数据。如果您觉得有帮助，请点赞分享。Vinesh 签字，再见。<br>
<br>原文链接：<a href="https://medium.com/javarevisited/prometheus-grafana-setup-to-visualize-your-servers-924773b83f3f">Prometheus + Grafana Setup To Visualize Your Servers — 2020</a> (翻译：xiebo)
                                
                                                              
</div>
            