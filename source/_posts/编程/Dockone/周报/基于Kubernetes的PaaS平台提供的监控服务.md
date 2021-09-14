
---
title: '基于Kubernetes的PaaS平台提供的监控服务'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/d29b6095e5779d000eb3fe161e57c195.jpg'
author: Dockone
comments: false
date: 2021-09-14 06:10:05
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/d29b6095e5779d000eb3fe161e57c195.jpg'
---

<div>   
<br><h3>概述</h3>我一直在负责维护的PaaS平台引入了Kubernetes作为底层支持，可以借助Kubernetes的生态做更多的事情，这篇博客主要介绍如何为普通用户提供图表监控服务（承接上一篇<a href="http://dockone.io/article/2434590">提供Dashboard支持</a>）。默认读者有能力自己搭建<code class="prettyprint">Kubernetes</code>集群以及初级的监控系统，以及可以简单的使用<code class="prettyprint">PromQL</code>，因为博客主要想介绍的内容不在此。<br>
<br><blockquote><br>我早于Dashboard就增加了这个功能，但是讲解起来实在复杂。一直拖着没写，今天有空，正好来分享一下吧。</blockquote><h3>方案拓扑</h3>这里我懒一下，不想画图了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/d29b6095e5779d000eb3fe161e57c195.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/d29b6095e5779d000eb3fe161e57c195.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
图中是整个方案的左半边，由采集工具采集机器以及容器信息，上传至<code class="prettyprint">Prometheus</code>中，右下角的<code class="prettyprint">Grafana</code>通过<code class="prettyprint">PromQL</code>查询以及展示数据，下面两个部分会简单介绍<code class="prettyprint">Prometheus</code>以及<code class="prettyprint">Grafana</code>，但重点在后面哈。<br>
<h3>朴素的收集与展示工具Prometheus</h3>这是一张Ingress的CPU利用率统计图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/1d66753a35ad72583a2cc83190dd11e0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/1d66753a35ad72583a2cc83190dd11e0.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
朴素的原因主要是这个工具做作用是收集数据，每次只能查询一条语句，而且没有什么历史记录功能，权限控制几乎没有，这样基础的工具肯定不能直接提供给用户。<br>
<h3>漂亮的展示工具Grafana</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/229e809533f8787e4643069967e6e53b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/229e809533f8787e4643069967e6e53b.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
相比上面简陋的图片，<code class="prettyprint">Grafana</code>的功能就强大很多了，可以展示多张图表，而且有了权限控制，非常适合建立大盘监控，对于<code class="prettyprint">PaaS</code>平台中的每个用户来讲，看到自己应用的监控是多么美妙的一件事。<br>
<br>-----------<br>
<br>如果仅仅是介绍到这里，大家在自己的Kubernetes集群中鼓捣一下应该很快就可以用了，我们既然作为PaaS平台的开发者，自然要考虑多用户以及多应用的组织管理方式，呈现给用户需要的资料的同时，也要保证用户以及应用间不会相互影响。没错这与上一篇<a href="http://dockone.io/article/2434590">Dashboard支持方案</a>类似，也要进行权限设计以及控制。<br>
<h3>权限同步策略</h3><h4>PaaS平台的权限系统</h4>在PaaS平台中，假设我们有一个用户A，他拥有自己的一个或多个应用群组（G1，G2），每个群组中部署了一系列应用程序（a1，a2……）。<br>
<h4>Grafana中的权限系统</h4>在Grafana权限系统中，有一些Teams，用户可以属于一个或多个Team。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/44feaf55b869a400645923742c566c88.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/44feaf55b869a400645923742c566c88.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
每个Folder可以拥有一个或多个Dashboard。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/1d0fcd35d05635bb4b8cf6ea5197e77e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/1d0fcd35d05635bb4b8cf6ea5197e77e.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>映射</h4>考虑到上述的关系，我们的思路就很明确了，我的设计方案是：<br>
<ol><li>用户的每个群组对应一个Team，该Team拥有一个Folder的访问权限</li><li>每个应用拥有一个Dashboard</li></ol><br>
<br>你也可以使用别的设计方案（比如说不要<code class="prettyprint">Folder</code>，每个Team拥有一些Dashboard），上述方案只是我想方便管理，每个Team拥有自己的Folder。<br>
<h3>Grafana相关类库及其使用</h3>我用的是<code class="prettyprint">Python</code>定时同步权限以及图表信息，当时也想过用<code class="prettyprint">Golang</code>，但我说真的，这种代码用<code class="prettyprint">Python</code>太适合了。下面的部分太过于偏了，建议不要去纠结，你大概率用不上，肯定要自己去读文档的。<br>
<pre class="prettyprint">grafana-api==1.0.3  # 用来与Grafana API通信  <br>
grafanalib==0.5.7   # 创建Grafana图表<br>
</pre><br>
<h4>User，Team，Folder创建</h4><pre class="prettyprint"># 下面是一个team的创建，其他类似<br>
def ensure_team(g_api, team_name):<br>
team_id = -1<br>
try:<br>
    # &#123;'message': 'Team created', 'teamId': 121&#125;<br>
    g_team = g_api.teams.add_team(&#123;'name': team_name&#125;)<br>
    team_id = g_team['teamId']<br>
except GrafanaClientError as e:<br>
    if e.status_code == 409:<br>
        # 'Client Error 409: Team name taken'<br>
        g_team = g_api.teams.get_team_by_name(team_name)[0]<br>
        team_id = g_team['id']<br>
assert team_id != -1<br>
return team_id<br>
</pre><br>
<h4>Folder与Team权限同步</h4><pre class="prettyprint"># 下面是同步team以及其用户，因为用户有可能增减，需要对应的增减<br>
def sync_user_team(g_api, team_id, user_ids):<br>
orig_members = g_api.teams.get_team_members(team_id)<br>
now_user_ids = set(user_ids)<br>
orig_user_ids = set([u['userId'] for u in orig_members])<br>
<br>
for user_id in now_user_ids - orig_user_ids:<br>
    try:<br>
        g_api.teams.add_team_member(team_id, user_id)<br>
    except GrafanaBadInputError:<br>
        pass<br>
<br>
for user_id in orig_user_ids - now_user_ids:<br>
    g_api.teams.remove_team_member(team_id, user_id)<br>
<br>
# 下面是同步folder以及team权限，所有普通用户只有只读权限<br>
def sync_folder_permission(folder, team_id=None):<br>
# https://grafana.com/docs/grafana/latest/http_api/folder_permissions/<br>
g_api = get_grafana_api()  # type: GrafanaFace<br>
permissions = []<br>
if team_id != None:<br>
    permissions.append(&#123;<br>
        "teamId": team_id,<br>
        "permission": 1  # 只有查看权限<br>
    &#125;)<br>
<br>
g_api.folder.update_folder_permissions(<br>
    folder['uid'],<br>
    &#123;<br>
        "items": permissions,<br>
    &#125;<br>
) <br>
</pre><br>
<h4>Dashboard页面设计以及同步</h4>这部分其实挺难的，我想使用类似声名式的写法，类似<code class="prettyprint">kubectl apply -f xxx.yaml</code>，不过<code class="prettyprint">Grafana</code>的API太难用了，一种解决方案是：导入Dashboard图表数据，可以看到我这里的API都是手动加的。<br>
<pre class="prettyprint">def sync_dashboard_data(dashboard_uid, folder_id, dashboard_json_data, inputs=[]):<br>
"""同步dashboard的组信息以及dashboard的pannel数据信息<br>
"""<br>
g_api = get_grafana_api()  # type: GrafanaFace<br>
d = g_api.dashboard.get_dashboard(dashboard_uid)<br>
<br>
data = &#123;<br>
    'dashboard': dashboard_json_data,<br>
    'folderId': folder_id,<br>
    "inputs": inputs,<br>
    'overwrite': True<br>
&#125;<br>
put_dashboard_path = "/dashboards/import"<br>
r = g_api.api.POST(put_dashboard_path, json=data)<br>
<br>
# 数据样式的生成请参考这里：<br>
# https://github.com/weaveworks/grafanalib/blob/master/grafanalib/tests/examples/example-elasticsearch.dashboard.py<br>
</pre><br>
<h3>最终效果</h3>针对我们系统中的每个应用，基本都有这么一张图表：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/89c2cc12bceb71168146d54b6ff4dcb6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/89c2cc12bceb71168146d54b6ff4dcb6.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>常用的图表推荐</h3>我平时作为管理员一般也不会看每个应用，可能看个大概吧。<br>
<h4>Ingress</h4><a href="https://github.com/kubernetes/ingress-nginx/blob/master/deploy/grafana/dashboards/nginx.json" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... .json</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/fc984c5fb3d4462a26daeb08dc2cec36.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/fc984c5fb3d4462a26daeb08dc2cec36.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>node_exporter</h4><a href="https://github.com/rfrail3/grafana-dashboards/blob/master/prometheus/node-exporter-full.json" rel="nofollow" target="_blank">https://github.com/rfrail3/gra ... .json</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/751945159c8dca386b250dbaf133d82b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/751945159c8dca386b250dbaf133d82b.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>总结</h3>这篇文章我主要想介绍下我们的系统是如何设计的，希望能够在大家设计系统接入方案时能有所参考，也欢迎大家留言讨论。<br>
<br>顺便吐槽一下<code class="prettyprint">Grafana</code>，居然不能设置URL头像（为了改头像我都去读Grafana代码了，发现不能修改），真是令人生气！<br>
<br>原文链接：<a href="https://corvo.myseu.cn/2021/01/06/2021-01-" rel="nofollow" target="_blank">https://corvo.myseu.cn/2021/01/06/2021-01-06-</a>基于Kubernetes的PaaS平台提供的监控服务/，作者：corvofeng
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            