
---
title: 'Viper for Nacos v0.4.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=882'
author: 开源中国
comments: false
date: Fri, 30 Jul 2021 11:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=882'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:left">v0.4.0更新：</h2> 
<p style="text-align:start">添加新的配置变更函数：</p> 
<pre><code class="language-go">WatchRemoteConfigOnChannel(remoteViper *viper.Viper) <-chan bool</code></pre> 
<p style="text-align:start"><span style="color:#333333">v0.3.0更新：</span></p> 
<p style="text-align:left">升级依赖： viper v1.8.1</p> 
<p style="text-align:left">此版本解决了 viper老版本中依赖etcd的问题，由于etcd v3.5.0 解决了模块化的问题；</p> 
<p style="text-align:left">这一版中我们可以同时集成grpc 、etcd 的最新版本。</p> 
<h2 style="text-align:left"><span style="color:#2c3e50">Viper remote</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F14721506.html%232351353687" target="_blank"><span style="color:#2c3e50">#</span></a></h2> 
<p style="text-align:left"><span style="color:#2c3e50">在Viper中启用远程支持，需要在代码中匿名导入viper/remote这个包。</span></p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#d73a49"><span style="color:#d73a49">import</span></span> _ <span style="color:#032f62"><span style="color:#032f62">"github.com/spf13/viper/remote"</span></span></code></pre> 
<p style="text-align:left"><span style="color:#2c3e50">通过remote,Viper将支持读取从Key/Value存储( 例如etcd或Consul或本文中的Nacos ).</span></p> 
<h3 style="text-align:left"><span style="color:#2c3e50">Viper加载配置值的优先级</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F14721506.html%2339802934" target="_blank"><span style="color:#2c3e50">#</span></a></h3> 
<p style="text-align:left"><span style="color:#2c3e50"><strong>磁盘上的配置文件 > 命令行标志位 > 环境变量 > 远程Key/Value存储 > 默认值</strong> 。</span></p> 
<h2 style="text-align:left"><span style="color:#2c3e50">Nacos 支持</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Fmaxzhang1985%2Fp%2F14721506.html%233100166811" target="_blank"><span style="color:#2c3e50">#</span></a></h2> 
<p style="text-align:left"><span style="color:#2c3e50">引用我们的开源库 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyoyofxteam%2Fnacos-viper-remote" target="_blank"><span style="color:#2c3e50">https://github.com/yoyofxteam/nacos-viper-remote</span></a></p> 
<pre style="text-align:left"><code class="language-go"><span style="color:#d73a49"><span style="color:#d73a49">import</span></span> (
<span style="color:#032f62"><span style="color:#032f62">"github.com/spf13/viper"</span></span>
remote <span style="color:#032f62"><span style="color:#032f62">"github.com/yoyofxteam/nacos-viper-remote"</span></span>
)</code></pre> 
<p style="text-align:left"><span style="color:#2c3e50">在项目中使用:</span></p> 
<pre><code class="language-go">config_viper := viper.New()

remote.SetOptions(&remote.Option&#123;
   Url:         "localhost",
   Port:        80,
   NamespaceId: "public",
   GroupName:   "DEFAULT_GROUP",
   Config: remote.Config&#123; DataId: "config_dev" &#125;,
   Auth:        nil,
&#125;)

remote_viper := viper.New()
err := remote_viper.AddRemoteProvider("nacos", "localhost", "")
remote_viper.SetConfigType("yaml")
err = remote_viper.ReadRemoteConfig()    //sync get remote configs to remote_viper instance memory . for example , remote_viper.GetString(key)

if err == nil &#123;
    config_viper = remote_viper
    fmt.Println("used remote viper")
    provider := remote.NewRemoteProvider("yaml")
    respChan := provider.WatchRemoteConfigOnChannel(config_viper)

    go func(rc <-chan bool) &#123;
        for &#123;
            <-rc
            fmt.Printf("remote async: %s", config_viper.GetString("yoyogo.application.name"))
        &#125;
    &#125;(respChan)
&#125;

go func() &#123;
    for &#123;
        time.Sleep(time.Second * 30) // delay after each request
        appName = config_viper.GetString("yoyogo.application.name")
        fmt.Println("sync:" + appName)
    &#125;
&#125;()</code></pre> 
<h3 style="text-align:left"><span style="color:#2c3e50">此项目已集成到 yoyogo</span></h3> 
<p style="text-align:left"><a href="https://gitee.com/yoyofx/yoyogo">https://gitee.com/yoyofx/yoyogo</a></p> 
<p style="text-align:left"> </p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#40485b">🦄🌈 YoyoGo 一个简单、轻量、快速、基于依赖注入的微服务框架( web 、grpc、xxl-job、console ),支持的注册中心 Nacos/Consoul/Etcd/Eureka/k8s 等。</span></p>
                                        </div>
                                      
</div>
            