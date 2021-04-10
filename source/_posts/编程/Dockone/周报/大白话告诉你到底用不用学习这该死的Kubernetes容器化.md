
---
title: '大白话告诉你到底用不用学习这该死的Kubernetes容器化'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210410/3e41443ccbbb2fde813ad8db4b4680f4.png'
author: Dockone
comments: false
date: 2021-04-10 08:08:23
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210410/3e41443ccbbb2fde813ad8db4b4680f4.png'
---

<div>   
<br><strong>运维就是要无所不懂，无所不知。</strong><br>
<br>今天分享最近集团  <code class="prettyprint">All In 容器化</code> 的工作心得。<br>
<br>虽然大家都是技术出身，但我依然会用尽可能用大白话来描述 <code class="prettyprint">Kubernetes</code> 和容器化，尽可能不带代码。因为在上云的过程中，我发现，即使是有技术背景的同学，也并非所有人能很好的掌握 <code class="prettyprint">Kubernetes</code>  和容器化。<br>
<h3>容器化背景介绍</h3><h4>初识 Docker</h4>个人其实接受容器化的时间算比较早的。大概 2014 年就已经接触，并有心在公司业务中实践。<br>
<br>工作时间比较长的朋友可能知道，那个时间节点，商业公司 <code class="prettyprint">EXSI</code> 早已经一统江湖，一家独大。而开源界的 <code class="prettyprint">KVM</code> 和 <code class="prettyprint">XEN</code> 的半虚拟化之争刚刚结束，做为 <code class="prettyprint">RedHat</code> 亲儿子的 <code class="prettyprint">KVM</code> 也逐渐独步青云。在开源领域独领风骚。<br>
<br><code class="prettyprint">XEN</code> 终究成为历史，成为过往，虽然生的早，但亲爹不行，又没有干爹，只能暗然退场。从此，江湖再无 <code class="prettyprint">XEN</code> 的身影。<br>
<br>彼时，<code class="prettyprint">Docker</code> 还是一个小啰啰，还在为活着而战，每天都是生死一线。彼时 <code class="prettyprint">Docker</code> 还不叫 <code class="prettyprint">Moby</code>（Docker 项目改名为 Moby）。<br>
<br>我当时供职的公司也不例外，使用 <code class="prettyprint">KVM</code> 管理着公司的所有应用和服务。就着对新技术的尝试，我“大「盲」胆「目」”的将 <code class="prettyprint">KVM</code> 的技术栈全线改为 <code class="prettyprint">Docker</code>，但仅仅一周不到，就发现严重的问题，发现团队人员的技术储备远远不够， <code class="prettyprint">Docker</code>  当时还有诸多问题，其次该技术栈仅运维单团队模块掌握还远远不够。必须是<strong>自上而下</strong>的贯彻实施，才有可能完成。<br>
<br>考量再三，当时立刻下架所有容器化技术。转回 <code class="prettyprint">KVM</code> 技术栈。现在想想，当时真的是 <code class="prettyprint">Too Young Too Simple</code>。<br>
<h4>再识 Docker</h4>再之后大概有 4 年没有再接触 <code class="prettyprint">Docker</code> 技术。一方面是创业项目和 <code class="prettyprint">Docker</code> 无关，再者是后来供职的公司或是创业阶段不合适，或是对新技术比较排斥。<br>
<br>时间一晃，2019 年底，我们有幸再次接触容器化技术。期间因为集团高层的频繁变动，容器化规划也一再被搁浅，个人因为一些原因也有离开的想法。幸运的是，2020 年中，<code class="prettyprint">ALL IN</code> 的技术战略终于被抬上桌面，且作为集团层面技术战略执行。每个团队都有容器化 <code class="prettyprint">KPI</code> 考核。<br>
<br>这简直就是冷宫坐尽，柳暗花明 ，<strong>机会不一定是争取来的，也可能是等出来的</strong>。真的是<strong>剩者</strong>为王呀！<br>
<br>随后就是为期不到 2 个月的紧张筹备。而此时，我们还有很多东西没有开始：<br>
<ol><li>云平台选型</li><li>架构迁移方案</li><li>网络及混合云共存方案</li><li>零 Kubernetes 线上经验</li><li>技术及人员储备严重不足</li></ol><br>
<br>其中，第 5 条最为致命，因为需要和时间赛跑。Kubernetes 的技术人员，也就我和另外一个技术同学，且经验都严重欠缺。<br>
<br>但容器化这样的天时、地利、人和的机会，错过就不可能再有第二次，所以大家都很拼。<br>
<br>这当然少不了，上层老板的资源倾斜，以及团队内其它同学主动承担日常工作，还有其它团队同学的大力支持和大开便利之门。才得以让整个项目在最后一刻压点上线。<br>
<br>好的，到此，感谢大家听完我唠叨完背景。下面为大家介绍技术性内容，可能比较枯燥，但请谅解且相信，我已经努力大白化了。<br>
<h3>公司现有架构和上云后的架构</h3>前面有提到，因为高层的频繁变动。所以技术战略一直在变，上云，下云，再上云，再下云……<br>
<br>不要以为这是故事，如果是故事，也是真的故事……就发生在我们身上。<br>
<br>在 <code class="prettyprint">ALL IN</code> 容器化的前一刻，我们的部分业务正在筹备下云……其它业务也像待宰的羔羊，怒气值爆满，但也只能是被屠宰的命。所以，我们架构比较乱。希望，你能懂……我梳理了上云前部分业务的架构。是如下这样的：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210410/3e41443ccbbb2fde813ad8db4b4680f4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210410/3e41443ccbbb2fde813ad8db4b4680f4.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>上云前架构简图 2</em><br>
<br>大致提几点：<br>
<ol><li>混合云架构，专线打通</li><li>经过几轮调整后的中台战略，各业务之间的相互调用还相对规范了那么一点。</li><li>信安在金融行业的特殊地位，在公司有着“太子军”的特权。</li></ol><br>
<br>作为第一批容器化的项目，我们挑选的标准也比较简单：<br>
<ol><li>非核心业务系统</li><li>技术栈尽可能简单</li><li>新业务</li><li>业务尽可能有代表性，如：和周边接口有着丰富的调用关系</li></ol><br>
<br>容器化后，我们的规划的初期架构如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210410/8027bb47f9156986afc56b28ecbe92b4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210410/8027bb47f9156986afc56b28ecbe92b4.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>上云后架构</em><br>
<br>提炼几个关键点：<br>
<ul><li>按功能分区</li><li>VPC，防火墙，Pod 不同级别的隔离均有</li><li>上网需求和非上网需求没有使用 Proxy 的方式，而是使用 VPC 的方式隔离</li><li><code class="prettyprint">Kubernetes</code> 的 <code class="prettyprint">svc</code> 使用 <code class="prettyprint">ClusterIP</code> 的模式，<code class="prettyprint">Cluster</code> 使用阿里云自有的 <code class="prettyprint">SLB</code> 分流并实现全模块高可用。</li></ul><br>
<br>具体上云过程太过细节，这里不一一介绍，必然是问题多多，但总体比我们想像的要容易且顺利。这里分享一些实践经验。<br>
<h3>经验分享</h3>大家知道，<code class="prettyprint">Kubernetes</code> 提供的是解决方案，而且是各个技术细分领域的成套解决方案，比如：存储解决方案，日志收集解决方案，高可用解决方案，分布式解决方案、CI/CD解决方案、横纵向解决方案等等。<br>
<br>这意味着，你单纯对 <code class="prettyprint">Kubernetes</code> 技术掌握的深浅只能决定你的熟练程度，而并非架构和项目解决能力。也意味着，除非从物理硬件、到系统底层、到网络架构、到 <code class="prettyprint">AP</code> 应用、到 <code class="prettyprint">HA</code>，<code class="prettyprint">HP</code> 你都有实践应用，才能在一时间做出正确的决策。<br>
<br>这也意味着，第一次容器化上云，如果没有额外的技术支持。很容易踩坑。<br>
<br>我们第一期容器化规划了 11 个项目。这次还是有一些内容可以和大家分享下，主要从如下几个方面：<br>
<ul><li>安全经验分享</li><li>规范经验分享</li><li>网络经验分享</li><li>镜像经验分享</li><li>流程经验分享</li><li>监控经验分享</li><li>存储经验分享</li></ul><br>
<br>下面一一为大家介绍。<br>
<h4>安全经验分享</h4>容器化之前，进程通信主要有：<br>
<ul><li>跨主机网络通信</li><li>同主机进程间通信</li></ul><br>
<br>安全主要关注：<br>
<ul><li>代码安全规范</li><li>开源软件网络高危漏洞</li><li>防止内鬼</li><li><code class="prettyprint">IDC</code> 环境及流量安全等</li></ul><br>
<br>使用 <code class="prettyprint">Kubernetes</code> 后，因为 <code class="prettyprint">IP</code> 不固定，安全的管控带来了一些不便利。但对于非金融行业的传统互联网公司，如果不需要精细管控进出口流量，其实容器化，还是提供了很好的便利。如针对 <code class="prettyprint">apiserver</code> 的安全攻击。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210410/7f66b7f34b5bebbc3e17a294dca32b22.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210410/7f66b7f34b5bebbc3e17a294dca32b22.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>apiserver 的安全攻击</em><br>
<br>改用 <code class="prettyprint">Kubernetes</code> 后，问题除了上面这些，又增加了：<br>
<ul><li>数据落地，数据是金融公司的命脉，落地到阿里云的存储上，公司并不放心，或者并不符合安全规范。</li><li>安全最小化原则，原来的网络权限最小化原则端到端并不适用，现在需要段到段。</li><li><code class="prettyprint">Kubernetes</code> 安全，如果 <code class="prettyprint">Kubernetes</code> 使用的是托管，那么所有的数据经过 <code class="prettyprint">apiserver</code> 时，均会被记录。<code class="prettyprint">apiserver</code> 需被重点保护，或者所有数据流经过类似 <code class="prettyprint">kms</code> 加密后使用。但同步会增加业务的开发成本和使用习惯。</li><li>镜像安全，安全团队并不一定具备精深容器化能力。<code class="prettyprint">Dockerfile</code> 或者 <code class="prettyprint">docker commit</code> 等如果流程不规范，存在较大<strong>"内鬼"</strong>安全隐患。</li></ul><br>
<br>如上。<br>
<br>解决方案如下，但不一定每家公司都有能力落地，或者有能力实施：<br>
<br><strong>零信任管理</strong><br>
<ul><li>零信任安全模型下没有绝对的安全域</li><li>在暴露的服务前设置尽可能多的防护层，实现纵深防御</li><li>权限配置和凭证下发遵循权限最小化原则</li><li>最小化攻击面</li></ul><br>
<br><strong>精细管理访问控制</strong><br>
<ul><li>在云资源控制平面，遵循权限最小化原则合理分配云账号的资源访问权限</li><li>在Kubernetes集群数据平面，根据业务场景，通过 Namespace 实现人员/应用/部门之间的逻辑隔离</li><li>使用 RBAC 进行资源模型维度的细粒度访问控制及时吊销或轮转可能泄露的访问凭证</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210410/bef1ad282c5e18ec3349f5aad91696e8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210410/bef1ad282c5e18ec3349f5aad91696e8.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Kubernetes RBAC 权限管理</em><br>
<br><strong>Pod 通信网络管理</strong><br>
<br>控制容器入网流量：<br>
<ol><li>限定容器允许监听的指定协议，端口和服务标签等</li><li>限定除 LB 和 Ingress 关联的服务外不允许外网 IP 访问</li><li>限定容器只允许其服务消费者访问</li></ol><br>
<br>控制容器出网流量：<br>
<ol><li>禁止不需要访问公网的Pods出网流量</li></ol><br>
<br><strong>日志审记</strong><br>
<ul><li>基础设施日志，云平台资源操作审计，云服务账号操作审计等；</li><li>Kubernetes 集群日志，集群 control-plane 组件日志，control-plane 组件审计日志（secrets 审计，apiserver 非法访问，exec 进入容器等操作审计）；</li><li>系统运维日志，主机层应用操作和运维审计；</li><li>应用日志，容器内应用进程日志。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210410/ad570798e7a72ddb6ffd83e5e5354304.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210410/ad570798e7a72ddb6ffd83e5e5354304.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Kubernetes 阿里云审记</em><br>
<br><strong>数据安全</strong><br>
<ul><li>全链路传输加密，系统组件，服务之间的全链路数据传输加密，敏感数据落盘加密</li><li>密钥管理：密钥的保护和轮转 DEK（数据加密密钥）和 KEK（密钥加密密钥）隔离</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210410/2816bd2a00b6ed920a1b4dd3a8c63616.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210410/2816bd2a00b6ed920a1b4dd3a8c63616.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>数据加密传输</em><br>
<h4>规范经验分享</h4>主要的坑有如下：<br>
<ol><li><code class="prettyprint">namespace</code> 过多，管理混乱</li><li><code class="prettyprint">namespace</code> 命名混乱，无法辨识</li><li><code class="prettyprint">yaml</code> 命名混乱，存放混乱</li><li>日志存储及收集优劣不清，无法选择最佳方案</li></ol><br>
<br>对应的方案如下文：<br>
<br><strong>namespace</strong><br>
<ul><li>按系统 <code class="prettyprint">Pod</code> 数量做规划</li><li>namespace 命名需流程规范化，运维有一票否决权</li><li>命名需要有明确特征。如工作类（tools），存储类（store），数据库类（db）</li></ul><br>
<br><strong>存储</strong><br>
<ul><li>日志存放<strong>必须</strong>从 <code class="prettyprint">Pod</code> 映射出来</li><li>日志禁止打印标准输出</li><li>日志建议存储两类：本地 + 网络（sidecar+ELK）</li><li>日志统一存放目录摆放规范：<code class="prettyprint">/naspath/[data|log|config|sharedata]/namespace/NodeName_PODName/</code></li></ul><br>
<br><strong>yaml</strong><br>
<ul><li><strong>禁止</strong>手动映射 <code class="prettyprint">nodeport</code>，防止端口冲突</li><li>命名：<code class="prettyprint">/usr/local/k8s/projectName/&#123;00-namespace.yaml,01-pv.yaml,02-pvc.yaml,03-svc.yaml,04-configmap.yaml,05-deployment.yaml,06-ingress.yaml&#125;</code></li><li>需有明确的<strong>资源限制</strong></li><li><code class="prettyprint">yaml</code> 需统一 <code class="prettyprint">GitLab</code> 管理</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210410/897e1ca7f70422bfc2d6e2f6890ec20a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210410/897e1ca7f70422bfc2d6e2f6890ec20a.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>资源限制</em><br>
<h4>镜像经验分享</h4>常见的坑：<br>
<ul><li>权限太大，任何人可推送</li><li>不做定期清理，导致仓库太大，存储压力过大</li><li>镜像命名规范不成熟</li><li>镜像层数过多</li><li>镜像过大</li></ul><br>
<br>对应的解决方案：<br>
<ul><li>各系统服务镜像统一存放在集团镜像仓库中</li><li>如需要开通权限可联系应用运维负责人</li><li>镜像的命名规则如下：harbor.company.com/项目名称/服务名称</li><li>强制定期清理</li><li>使用轻量化的基础镜像，e.g. distroless镜像</li><li>不要构建过大或层数过多的镜像</li><li>删除基础镜像中的包管理或网络工具</li><li>删除文件属性修改工具（chmod，chown）</li><li>不要轻易部署公共仓库的镜像</li><li>不要使用 root 用户启动镜像</li><li>可以使用 Ephemeral 临时容器 debug（Alpha as of 1.16）</li><li>伪代码如下：</li></ul><br>
<br><pre class="prettyprint">FROM python:3.6.12-slim  <br>
LABEL maintainer="mail.com"  <br>
LABEL project="project-name"  <br>
<br>
ENV MODULE_NAME="orangutan.server"  <br>
<br>
# copy contents of project into docker  <br>
COPY ./code/ /app/  <br>
<br>
WORKDIR /app  <br>
<br>
RUN pip install --upgrade pip \  <br>
&& pip install poetry \  <br>
&& poetry config virtualenvs.create false \  <br>
&& poetry install  <br>
<br>
COPY ./sources.list /etc/apt/  <br>
<h1>RUN mv /var/lib/dpkg/info /var/lib/dpkg/info_bak \</h1>RUN rm -rf /var/lib/dpkg/info \  <br>
#    && mkdir /var/lib/dpkg/info/ \  <br>
&& mkdir -p /var/lib/dpkg/info \  <br>
&& apt-get update \  <br>
&& apt-get -f install \  <br>
&& apt-get update \  <br>
&& apt-get install -y dialog \  <br>
&& apt-get install -y libreoffice xfonts-wqy \  <br>
&& apt-get clean  <br>
<br>
CMD ["uvicorn", "main:contract", "--host", "0.0.0.0", "--port", "80"]  <br>
</pre><br>
<h4>流程经验分享</h4>常见的坑：<br>
<ul><li>为了进度牺牲流程和品控</li><li>代码开发不在容器中进行</li><li>开发不会写 <code class="prettyprint">Dockerfile</code></li><li><code class="prettyprint">CI/CD</code>平台无法使用</li></ul><br>
<br>对应的解决方案：<br>
<ul><li>事先规划项目，引入 PM 管理制度，每日站会。实时同步问题及进度</li><li>自上而下引入容器化技术，争取足够资源</li><li>事先提供成熟可靠的容器化环境，供开发使用。</li><li>事先约定好各方职责及工作内容。普及容器化基础和运营理念</li><li>前期运维和开发共同编写 <code class="prettyprint">Dockerfile</code>，后期开发写，运维优化审核</li><li>考虑到时间和技术成本，前期不建议纯自研的 <code class="prettyprint">CI/CD</code>。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210410/1f0d2a6d9b6bcdac7739c5dcd6da5b9b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210410/1f0d2a6d9b6bcdac7739c5dcd6da5b9b.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>CI、CD方案</em><br>
<h4>监控经验分享</h4>常见的坑：<br>
<ul><li>原有的方案 <code class="prettyprint">Zabbix</code> 或 <code class="prettyprint">CAT</code>需改造升级，新旧平台迁移难度大</li><li>原有短信、微信、电话告警接入全作废</li></ul><br>
<br>解决方案：<br>
<ul><li>新旧环境分离，网络互通，逐步迁移</li><li>尽可能使用云平台成套解决方案，退而求其次方案：Grafana + Prometheus + cAdvisor + Datadog（暂时未接入）</li><li><code class="prettyprint">Triger</code> 失效没有捷径， 只能重建</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210410/2abdeae541cd83acd36c00799fad78a5.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210410/2abdeae541cd83acd36c00799fad78a5.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Kubernetes 的 Prometheus 解决方案</em><br>
<h4>存储经验分享</h4><code class="prettyprint">Kubernetes</code> 支持的存储类型非常多，几乎覆盖市面常见存储类型：awsElasticBlockStore，CephFS， EBS，azureDisk，emptyDir，ConfigMap 等等，这里不赘述，详见官方。<br>
<br>使用哪种，具体参考业务类型，以阿里云为例，我们通常使用 3 种方案结合：<br>
<br><strong>NAS</strong><br>
<br>主要针对分布式存储场景的业务。比如日志，配置文件（阿里的技术工程师建议直接打到 Pod 里面），SVN，GitLab，db 的数据存放。等对分布式数据有要求的业务场景。<br>
<br><strong>优点</strong>：简单好用。横向、纵向几乎无限扩展。数据管理极为方便<br>
<br><strong>缺点</strong>：稍贵，但可接入<br>
<br><strong>建议</strong>：大部分场景直接使用NAS。<br>
<br><strong>高效云盘</strong><br>
<br>原来打算使用高效云盘，后来仔细盘算后，结合考虑人员技术门槛，数据存放规范等等场景，维护成本太大，且成本和 <code class="prettyprint">NAS</code> 相比，可接受。所以没有使用高效云盘，<strong>all in NAS</strong>。<br>
<br>优缺点：自己体会<br>
<br><strong>Anyshare</strong><br>
<br><code class="prettyprint">Anyshare</code> 是老旧业务使用的华为一款共享存储方案。后面会逐步使用 <code class="prettyprint">NAS</code> 或 <code class="prettyprint">OSS</code> 代替。<br>
<br><strong>OSS</strong><br>
<br>阿里云技术工程师力荐的日志及数据收集工具。<br>
<br>早期的日志解决方案是：app -> SLS -> 时序数据库 -> ELK 和 OSS<br>
<br>但考虑到<strong>金融行业的日志数据太重要，纯数据流的收集方式不安全</strong>。所以 PASS 了。使用了数据流 + 本地双重写的方式。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210410/caee94554596b5139dfceb5f1799f268.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210410/caee94554596b5139dfceb5f1799f268.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>阿里推荐的 sls 日志收集架构</em><br>
<br>因为涉及到的改造太大，同时因为单纯的流日志处理有日志丢失的隐患。所以我们优化了日志收集架构，使用的是张磊推荐的日志收集方案。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210410/a261dae4a4788b692186293316a1bfa0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210410/a261dae4a4788b692186293316a1bfa0.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>张磊推荐的日志收集方案</em><br>
<br>而且，在其方案的基础上。我们对存储方式做了进一步优化，使用分布式 NAS 存储。<br>
<h3>未来</h3>肯定有朋友会问，我们什么时候使用 lstio 或 Serverless 的更高级方案。<br>
<br>目前来看，Kubernetes 的容器化技术满足了我们现有的需要。云原生或者网络服务，我们会去技术尝鲜，有需求会考虑。<br>
<h3>其它更重要的一些人生建议</h3>好了，扯了这么多，终于可以扯回到题目了。<strong>大白话告诉你到底用不用学习这该死的 Kubernetes 容器化？</strong><br>
<ul><li>Kubernetes 什么时候合适使用？</li><li>Kubernetes 到底难不难？</li><li>Kubernetes 到底用不用学？</li></ul><br>
<br>真的是灵魂三问啊！<br>
<h4>Kubernetes 什么时候合适使用？</h4>我写过的文章里，已经重复讲过很多次。<br>
<br><strong>Kubernetes 不是一个开源软件，而是提供整套的运维架构方案解决。即 Kubernetes 的角色其实是运维架构师</strong>。你懂了吗？<br>
<br>那么什么时候用的到架构呢？架构是个很大的词。这也意味着，小规模的应用，基本可以考虑使用 <code class="prettyprint">Kubernetes</code>。但如果公司技术文化很前沿，那是一次使用 <code class="prettyprint">Kubernetes</code> 的良机，值得把握。<br>
<br>但如果公司比较传统，业务排期很紧张，又没有自上而下的资源支持。<strong>不建议单个部门独挑大梁，<code class="prettyprint">Kubernetes</code> 改变的不仅仅是运维的运维习惯，开发，测试，工具等等，所有的技术部门任何一个部门出差错，你都会死的很难堪</strong>。希望我讲明白了。<br>
<br>不跟风，不排斥。<br>
<br>最近阿里拆中台的事情，恐怕你也是知道的。一台鸡毛阿里最多难受下，小公司可能命就没了。<br>
<h4>Kubernetes 到底难不难？</h4>这个问题其实挺难回答的。<br>
<br>用老话讲，真的是“难者不会，会者不难”。但平心而论，我确实放弃过挺多次……但过了那道门槛，后面会发现。<code class="prettyprint">Kubernetes</code> 实在太厉害了。<br>
<br><strong>人体的本能就是喜欢舒适区，本能会排斥新事物。但请听我一句建议：既然选择了远方，便只顾风雨兼程。你还记得来时的路吗？</strong><br>
<h4>Kubernetes 到底用不用学？</h4>不要再骗自己了。最大的不变就是拥抱变化。<br>
<br>运维行业的未来只有行业专家岗和技术专家岗。单纯的业务岗只会慢慢轮为职能操作岗。至于管理岗，价值会越来越依赖公司的规模，纯管理的中低层会越来越难。这次疫情只是提前映射了未来的行情状况，看看你身边的那些失业的朋友，你会明白一点点。<br>
<br>Kubernetes 是一款伟大的产品，尽情去拥抱他吧！<br>
<br>参考： <br>
<ul><li><a href="https://www.liukui.tech/2019/01/15/Kubernetes-Promethues" rel="nofollow" target="_blank">https://www.liukui.tech/2019/0 ... thues</a>监控/</li><li>《容器安全最佳实践》</li><li>感谢 Google 的 Kubernetes 工程师</li></ul><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/zArZJvbVeUhUayLbIDK9FA" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/zArZJvbVeUhUayLbIDK9FA</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            