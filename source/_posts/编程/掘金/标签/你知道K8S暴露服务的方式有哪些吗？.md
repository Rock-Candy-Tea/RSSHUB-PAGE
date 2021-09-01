
---
title: '你知道K8S暴露服务的方式有哪些吗？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=1303'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 00:49:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=1303'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>Kubernetes</code>支持多种将外部流量引入集群的方法。<code>ClusterIP</code>、<code>NodePort</code>和<code>Ingress</code>是三种广泛使用的资源，它们都在路由流量中发挥作用。每一个都允许您使用一组独特的功能和折衷方案来公开服务。</p>
<h3 data-id="heading-0">背景</h3>
<p>默认情况下，<code>Kubernetes</code>上运行的服务都是在自己的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzNTY5MzU2MA%3D%3D%26mid%3D2247485464%26idx%3D1%26sn%3D00ca443bbcd4b2996efdede396b6c667%26chksm%3Dfa80d98fcdf7509944d63f618264e36cd8082a77e23aa36428a3d57a2f4189bcce4e52986967%26token%3D2075750696%26lang%3Dzh_CN%23rd" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzNTY5MzU2MA==&mid=2247485464&idx=1&sn=00ca443bbcd4b2996efdede396b6c667&chksm=fa80d98fcdf7509944d63f618264e36cd8082a77e23aa36428a3d57a2f4189bcce4e52986967&token=2075750696&lang=zh_CN#rd" ref="nofollow noopener noreferrer">Pod</a> 里过着与世隔绝的生活，外部无法打扰他们。我们可以通过创建  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzNTY5MzU2MA%3D%3D%26mid%3D2247486082%26idx%3D1%26sn%3D42a9bc8fcfc9da09445e9e2f4cf2fb96%26chksm%3Dfa80db15cdf752039494992f71a3bc488cf386841bd1aaaa44115f5e7f155ba55ce468ec89ee%26token%3D2075750696%26lang%3Dzh_CN%23rd" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzNTY5MzU2MA==&mid=2247486082&idx=1&sn=42a9bc8fcfc9da09445e9e2f4cf2fb96&chksm=fa80db15cdf752039494992f71a3bc488cf386841bd1aaaa44115f5e7f155ba55ce468ec89ee&token=2075750696&lang=zh_CN#rd" ref="nofollow noopener noreferrer">Service</a> 使容器供外部世界可见，这个“外部世界” 即可以整个集群、也可以是整个互联网。</p>
<p><code>Service</code>将流量路由到<code>Pod</code>内的容器中。<code>Service</code>是一种用于在网络上公开<code>Pod</code>的抽象机制。每个<code>Service</code>有一个类型——<code>ClusterIP</code>、<code>NodePort</code>或<code>LoadBalancer</code>。这些定义了外部流量如何到达服务。</p>
<p>但是光有<code>Service</code>也不行 ，有时候我们需要将不同域名和URL路径上的流量路由到集群内部，这就需要<code>Ingress</code>帮助才行。</p>
<h3 data-id="heading-1">ClusterIP</h3>
<p>ClusterIP 是默认的<code>Service</code>类型，不指定<code>Type</code>时默认就是<code>ClusterIP</code>类型的<code>Service</code>。<code>ClusterIP</code>在集群内提供网络连接。它通常无法从外部访问。我们将这些<code>ClusterIP Service</code>用于服务之间的内部网络。</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">apiVersion:</span> <span class="hljs-string">v1</span>
<span class="hljs-attr">kind:</span> <span class="hljs-string">Service</span>
<span class="hljs-attr">spec:</span>
<span class="hljs-attr">metadata:</span>
  <span class="hljs-attr">name:</span> <span class="hljs-string">my-service</span>
  <span class="hljs-attr">selector:</span>
    <span class="hljs-attr">app:</span> <span class="hljs-string">my-app</span>
  <span class="hljs-attr">type:</span> <span class="hljs-string">ClusterIP</span>
  <span class="hljs-attr">ports:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">http</span>
      <span class="hljs-attr">port:</span> <span class="hljs-number">80</span>
      <span class="hljs-attr">targetPort:</span> <span class="hljs-number">8080</span>
      <span class="hljs-attr">protocol:</span> <span class="hljs-string">TCP</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的示例定义了一个<code>ClusterIP Service</code>。到<code>ClusterIP</code> 上端口 80 的流量将转发到你的<code>Pod</code> 上的端口 8080  (targetPort配置项)，携带 <code>app: my-app</code>标签的 Pod 将被添加到 <code>Service</code>中作为作为服务的可用端点。</p>
<p>可以通过运行 <code>kubectl get svc my-service</code> 查看分配的 IP 地址。集群中的其他服务可以使用 10.96.0.1:80 与这个的 Service 管控的服务进行交互。</p>
<pre><code class="hljs language-shell copyable" lang="shell">➜  kubectl get svc app-service
NAME              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)           AGE
my-service        ClusterIP   10.96.0.1        <none>        8080:80/TCP       63d
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以使用 <code>spec.clusterIp</code> 字段手动将 ClusterIP 设置为特定 IP 地址：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">spec:</span>
  <span class="hljs-attr">type:</span> <span class="hljs-string">ClusterIP</span>
  <span class="hljs-attr">clusterIp:</span> <span class="hljs-number">123.123</span><span class="hljs-number">.123</span><span class="hljs-number">.123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">NodePort</h3>
<p><code>NodePort</code>在固定端口号上公开向集群外部暴露服务，它允许从集群外部访问该服务，在集群外部需要使用集群的 IP 地址和<code>NodePort</code>指定的端口才能访问。 创建<code>NodePort Service</code>将在集群中的每个<code>Node</code>上开放该端口。 <code>Kubernetes</code>会自动将端口流量路由到它所连接的服务。 下面是一个 <code>NodePort Service</code> 的示例：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">apiVersion:</span> <span class="hljs-string">v1</span>
<span class="hljs-attr">kind:</span> <span class="hljs-string">Service</span>
<span class="hljs-attr">spec:</span>
<span class="hljs-attr">metadata:</span>
  <span class="hljs-attr">name:</span> <span class="hljs-string">my-service</span>
  <span class="hljs-attr">selector:</span>
    <span class="hljs-attr">app:</span> <span class="hljs-string">my-app</span>
  <span class="hljs-attr">type:</span> <span class="hljs-string">NodePort</span>
  <span class="hljs-attr">ports:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">http</span>
      <span class="hljs-attr">port:</span> <span class="hljs-number">80</span>
      <span class="hljs-attr">targetPort:</span> <span class="hljs-number">8080</span>
      <span class="hljs-attr">protocol:</span> <span class="hljs-string">TCP</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>NodePort</code>的定义与<code>ClusterIP Service</code>具有相同的属性。唯一的区别是把类型设置成了："NodePort"。 <code>targetPort</code>字段仍然是必需的，因为<code>NodePort</code>由<code>ClusterIP</code>提供支持。</p>
<p>创建<code>NodePort Service</code>的同时还会自动创建一个<code>ClusterIP</code> 类型的<code>Service</code>，<code>NodePort</code>会将端口上的流量路由给<code>ClusterIP</code> 类型的 Service。</p>
<p>这也就是为什么下面我们查看<code>NodePort Service</code>时发现他也是有 ClusterIP 的原因：</p>
<pre><code class="hljs language-shell copyable" lang="shell">➜  kubectl get svc my-service
NAME              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)           AGE
my-service        NodePort    10.96.44.244     <none>        8080:30176/TCP    56d
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用上述例子创建<code>NodePort Service</code>，<code>Kubernetes</code>将会从30000-32767这个范围随机分配一个端口作为<code>NodePort</code>端口，不过我们可以通过设置<code>ports.nodePort</code>字段来手动指定端口：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">spec:</span>
  <span class="hljs-attr">ports:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">http</span>
      <span class="hljs-attr">port:</span> <span class="hljs-number">80</span>
      <span class="hljs-attr">targetPort:</span> <span class="hljs-number">8080</span>
      <span class="hljs-attr">nodePort:</span> <span class="hljs-number">32000</span>
      <span class="hljs-attr">protocol:</span> <span class="hljs-string">TCP</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个会将 32000 端口上的流量通过<code>Service</code>最终路由给<code>Pod</code>里容器的 8080 端口。</p>
<p>您可以使用<code>NodePort</code>快速设置用于开发环境的服务或在其上公开<code>TCP</code>或<code>UDP</code>服务，但是对于公开<code>HTTP</code>服务来说<code>NodePort</code>不是一个的理想选择，因为其使用的都是非<code>HTTP</code>标准的端口，我们需要使用其他替代方案。</p>
<h3 data-id="heading-3">Ingress</h3>
<p><code>Ingress</code> 实际上是与<code>Service</code>完全不同的资源，算是<code>Service</code>上面的一层代理，通常在 <code>Service</code>前使用<code>Ingress</code>来提供<code>HTTP</code>路由配置。它让我们可以设置外部 URL、基于域名的虚拟主机、SSL 和负载均衡。</p>
<p>给<code>Service</code>前面加<code>Ingress</code>，你的集群中需要有<code>Ingress-Controller</code>才行。有多种控制器可供选择。大多数主要的云提供商都有自己的<code>Ingress-Controller</code>，与他们的负载平衡基础设施相集成。如果是自建K8S集群，通常使用<code>nginx-ingress</code>作为控制器，它使用<code>NGINX</code>服务器作为反向代理来把流量路由给后面的<code>Service</code>。</p>
<blockquote>
<p>关于控制器Nginx-Ingress的安装部署，请参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fkubernetes.github.io%2Fingress-nginx%2Fdeploy%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://kubernetes.github.io/ingress-nginx/deploy/" ref="nofollow noopener noreferrer">kubernetes.github.io/ingress-ngi…</a> 后面介绍<code>Ingress</code>实践的文章也会再细说。</p>
</blockquote>
<p>可以使用<code>Ingress</code> 资源类型创建<code>Ingress</code>。 kubernetes.io/ingress.class 注释可让你指明正在创建的<code>Ingress</code>分类。如果集群里安装了多个<code>Ingress-Controller</code>这将很有用，也可以将不同的<code>Service</code>分别挂在不同分类的<code>Ingress</code>下面，增加一些高可用性。</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">apiVersion:</span> <span class="hljs-string">networking.k8s.io/v1beta1</span>
<span class="hljs-attr">kind:</span> <span class="hljs-string">Ingress</span>
<span class="hljs-attr">metadata:</span>
  <span class="hljs-attr">name:</span> <span class="hljs-string">my-ingress</span>
  <span class="hljs-attr">annotations:</span>
    <span class="hljs-attr">kubernetes.io/ingress.class:</span> <span class="hljs-string">nginx</span>
<span class="hljs-attr">spec:</span>
  <span class="hljs-attr">rules:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">host:</span> <span class="hljs-string">example.com</span>
      <span class="hljs-attr">http:</span>
        <span class="hljs-attr">paths:</span>
          <span class="hljs-bullet">-</span> <span class="hljs-attr">path:</span> <span class="hljs-string">/</span>
            <span class="hljs-attr">backend:</span>
              <span class="hljs-attr">serviceName:</span> <span class="hljs-string">my-service</span>
              <span class="hljs-attr">servicePort:</span> <span class="hljs-number">80</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">host:</span> <span class="hljs-string">another-example.com</span>
      <span class="hljs-attr">http:</span>
        <span class="hljs-attr">paths:</span>
          <span class="hljs-bullet">-</span> <span class="hljs-attr">path:</span> <span class="hljs-string">/</span>
            <span class="hljs-attr">backend:</span>
              <span class="hljs-attr">serviceName:</span> <span class="hljs-string">second-service</span>
              <span class="hljs-attr">servicePort:</span> <span class="hljs-number">80</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面定义了两个<code>Ingress</code>端点。第一个主机规则将 example.com 流量路由到<code>my-service</code>服务上的端口 80。第二条规则将 another-example.com 流量路由到<code>second-service</code>。</p>
<p>如果想使用 <code>HTTPs</code> 访问服务，可以通过在<code>Ingress</code> 规范中设置<code>tls</code>字段来配置 <code>SSL</code>：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">spec:</span>
  <span class="hljs-attr">tls:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">hosts:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">example.com</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">secretName:</span> <span class="hljs-string">my-secret</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过前提是在集群中需要通过<code>Secret</code>对象配置这些域名的证书信息。</p>
<p>当需要处理来自多个域名 和 URL 路径的流量时，应该使用<code>Ingress</code>。它让我们可以使用声明性语句配置路由和<code>Service</code>。<code>Ingress</code>控制器将提供你的路由并将它们映射到服务。</p>
<h3 data-id="heading-4">总结</h3>
<p><code>ClusterIP</code>、<code>NodePort</code>、<code>Ingress</code>将流量路由到集群中的服务。每一个都是为不同的用例设计的。<code>ClusterIP</code>更多是为集群内服务的通信而设计，某些向集群外部暴露的<code>TCP</code>和<code>UDP</code>服务适合使用<code>NodePort</code>。而如果向外暴露的是<code>HTTP</code>服务，且需要提供域名和<code>URL</code>路径路由能力时则需要在<code>Service</code>上面再加一层<code>Ingress</code>做反向代理才行。</p>
<p>可能你对<code>Ingress</code>，<code>Ingress-Controller</code>还是有一点模糊，后面我在写一篇<code>Ingress</code>的实践文章，给大家扫扫盲。</p>
<p>没有关注的同学，可以关注一下后面的文章动态。</p>
<h3 data-id="heading-5">相关阅读</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzNTY5MzU2MA%3D%3D%26mid%3D2247486082%26idx%3D1%26sn%3D42a9bc8fcfc9da09445e9e2f4cf2fb96%26chksm%3Dfa80db15cdf752039494992f71a3bc488cf386841bd1aaaa44115f5e7f155ba55ce468ec89ee%26token%3D2075750696%26lang%3Dzh_CN%23rd" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzNTY5MzU2MA==&mid=2247486082&idx=1&sn=42a9bc8fcfc9da09445e9e2f4cf2fb96&chksm=fa80db15cdf752039494992f71a3bc488cf386841bd1aaaa44115f5e7f155ba55ce468ec89ee&token=2075750696&lang=zh_CN#rd" ref="nofollow noopener noreferrer">学练结合，快速掌握K8S Service</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzNTY5MzU2MA%3D%3D%26mid%3D2247485464%26idx%3D1%26sn%3D00ca443bbcd4b2996efdede396b6c667%26chksm%3Dfa80d98fcdf7509944d63f618264e36cd8082a77e23aa36428a3d57a2f4189bcce4e52986967%26token%3D2075750696%26lang%3Dzh_CN%23rd" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzNTY5MzU2MA==&mid=2247485464&idx=1&sn=00ca443bbcd4b2996efdede396b6c667&chksm=fa80d98fcdf7509944d63f618264e36cd8082a77e23aa36428a3d57a2f4189bcce4e52986967&token=2075750696&lang=zh_CN#rd" ref="nofollow noopener noreferrer">K8S 里常提到的 Pod 是什么</a></li>
</ul>
<blockquote>
<p>今天的文章就到这里啦，如果喜欢我的文章就帮我点个赞吧，我会每周通过技术文章分享我的所学所见和第一手实践经验，感谢你的支持。<strong>微信搜索关注公众号--网管叨bi叨</strong>每周教会你一个进阶知识。</p>
</blockquote></div>  
</div>
            