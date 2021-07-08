
---
title: 'Viper for Nacos v0.3.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5949'
author: 开源中国
comments: false
date: Thu, 08 Jul 2021 19:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5949'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:left">v0.3.0更新：</h2> 
<p>升级依赖： viper v1.8.1</p> 
<p>此版本解决了 viper老版本中依赖etcd的问题，由于etcd v3.5.0 解决了模块化的问题；</p> 
<p>这一版中我们可以同时集成grpc 、etcd 的最新版本。</p> 
<h2 style="text-align:left"><span style="color:#2c3e50">Viper remote</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F14721506.html%232351353687" target="_blank"><span style="color:#2c3e50">#</span></a></h2> 
<p style="text-align:left"><span style="color:#2c3e50">在Viper中启用远程支持，需要在代码中匿名导入viper/remote这个包。</span></p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#d73a49">import</span> _ <span style="color:#032f62">"github.com/spf13/viper/remote"</span></code></pre> 
<p style="text-align:left"><span style="color:#2c3e50">通过remote,Viper将支持读取从Key/Value存储( 例如etcd或Consul或本文中的Nacos ).</span></p> 
<h3 style="text-align:left"><span style="color:#2c3e50">Viper加载配置值的优先级</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F14721506.html%2339802934" target="_blank"><span style="color:#2c3e50">#</span></a></h3> 
<p style="text-align:left"><span style="color:#2c3e50"><strong>磁盘上的配置文件 > 命令行标志位 > 环境变量 > 远程Key/Value存储 > 默认值</strong> 。</span></p> 
<h2 style="text-align:left"><span style="color:#2c3e50">Nacos 支持</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F14721506.html%233100166811" target="_blank"><span style="color:#2c3e50">#</span></a></h2> 
<p style="text-align:left"><span style="color:#2c3e50">引用我们的开源库 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyoyofxteam%2Fnacos-viper-remote" target="_blank"><span style="color:#2c3e50">https://github.com/yoyofxteam/nacos-viper-remote</span></a></p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#d73a49">import</span> (
<span style="color:#032f62">"github.com/spf13/viper"</span>
remote <span style="color:#032f62">"github.com/yoyofxteam/nacos-viper-remote"</span>
)</code></pre> 
<p style="text-align:left"><span style="color:#2c3e50">在项目中使用:</span></p> 
<pre style="text-align:left"><code class="language-go">runtime_viper := viper.New()
<span style="color:#6a737d">// 配置 Viper for Nacos 的远程仓库参数</span>
remote.SetOptions(&remote.Option&#123;
   Url:         <span style="color:#032f62">"localhost"</span>,            <span style="color:#6a737d">// nacos server 多地址需要地址用;号隔开，如 Url: "loc1;loc2;loc3"</span>
   Port:        80,                     <span style="color:#6a737d">// nacos server端口号</span>
   NamespaceId: <span style="color:#032f62">"public"</span>,               <span style="color:#6a737d">// nacos namespace</span>
   GroupName:   <span style="color:#032f62">"DEFAULT_GROUP"</span>,        <span style="color:#6a737d">// nacos group</span>
   Config: remote.Config&#123; DataId: <span style="color:#032f62">"config_dev"</span> &#125;, <span style="color:#6a737d">// nacos DataID</span>
   Auth:        <span style="color:#005cc5">nil</span>,                    <span style="color:#6a737d">// 如果需要验证登录,需要此参数</span>
&#125;)

err := remote_viper.AddRemoteProvider(<span style="color:#032f62">"nacos"</span>, <span style="color:#032f62">"localhost"</span>, <span style="color:#032f62">""</span>)
remote_viper.SetConfigType(<span style="color:#032f62">"yaml"</span>)

_ = remote_viper.ReadRemoteConfig()             <span style="color:#6a737d">//sync get remote configs to remote_viper instance memory . for example , remote_viper.GetString(key)</span>
_ = remote_viper.WatchRemoteConfigOnChannel()   <span style="color:#6a737d">//异步监听Nacos中的配置变化，如发生配置更改，会直接同步到 viper实例中。</span>

appName := remote_viper.GetString(<span style="color:#032f62">"key"</span>)   <span style="color:#6a737d">// sync get config by key</span>

fmt.Println(appName)

<span style="color:#6a737d">// 这里不是必须的，只为了监控Demo中的配置变化，并打印出来</span>
<span style="color:#d73a49">go</span> <span style="color:#d73a49">func</span>() &#123;
    <span style="color:#d73a49">for</span> &#123;
        time.Sleep(time.Second * 30) <span style="color:#6a737d">// 每30秒检查配置是否发生变化 </span>
        appName = config_viper.GetString(<span style="color:#032f62">"yoyogo.application.name"</span>)
        fmt.Println(appName)
    &#125;
&#125;()</code></pre> 
<h3 style="text-align:left"><span style="color:#2c3e50">些项目已集成到 yoyogo</span></h3> 
<p style="text-align:left"><a href="https://gitee.com/yoyofx/yoyogo">https://gitee.com/yoyofx/yoyogo</a></p> 
<p style="text-align:left"><span style="color:#2c3e50">🦄🌈 YoyoGo is a simple, light and fast , dependency injection based micro-service framework written in Go. Support Nacos ,Consoul ,Etcd ,Eureka ,kubernetes.</span></p>
                                        </div>
                                      
</div>
            