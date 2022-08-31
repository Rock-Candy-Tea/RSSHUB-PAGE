
---
title: 'Apache ShenYu 发布 2.5.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f90425f3d95446981de10a4143203b8~tplv-k3u1fbpfcp-watermark.image?'
author: 开源中国
comments: false
date: Wed, 31 Aug 2022 07:56:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f90425f3d95446981de10a4143203b8~tplv-k3u1fbpfcp-watermark.image?'
---

<div>   
<div class="content">
                                                                                            <h2>前言</h2> 
<p>时隔 4 个月，Apache ShenYu 迎来 2.5.0 的大版本，本次版本内容，共有 300 + 的 pull Request，60 + 的贡献者参与提交，88000 + 的添加或者修改的代码行数，该版本优化许多内容，让我们看下这个版本都做了什么。以下只是列举比较重要的一些功能。</p> 
<h3>日志功能</h3> 
<ul> 
 <li>新增对接阿里云SLS日志插件</li> 
</ul> 
<blockquote> 
 <p>具体使用参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshenyu.apache.org%2Fzh%2Fdocs%2Fplugin-center%2Fobservability%2Flogging-aliyun-sls%2F" target="_blank">https://shenyu.apache.org/zh/docs/plugin-center/observability/logging-aliyun-sls/</a></p> 
</blockquote> 
<ul> 
 <li>新增对接Elastic Search日志插件</li> 
</ul> 
<blockquote> 
 <p>具体使用参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshenyu.apache.org%2Fzh%2Fdocs%2Fplugin-center%2Fobservability%2Flogging-elasticsearch" target="_blank">https://shenyu.apache.org/zh/docs/plugin-center/observability/logging-elasticsearch</a></p> 
</blockquote> 
<ul> 
 <li>新增对接Apache RocketMQ日志插件</li> 
</ul> 
<blockquote> 
 <p>具体使用参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshenyu.apache.org%2Fzh%2Fdocs%2Fplugin-center%2Fobservability%2Flogging-rocketmq" target="_blank">https://shenyu.apache.org/zh/docs/plugin-center/observability/logging-rocketmq</a></p> 
</blockquote> 
<ul> 
 <li>新增对接Apache Kafka日志插件</li> 
</ul> 
<blockquote> 
 <p>具体使用参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshenyu.apache.org%2Fzh%2Fdocs%2Fplugin-center%2Fobservability%2Flogging-kafka" target="_blank">https://shenyu.apache.org/zh/docs/plugin-center/observability/logging-kafka</a></p> 
</blockquote> 
<h3>新功能</h3> 
<h4>新增 mock 插件。</h4> 
<p>为请求指定响应状态码和响应体方便进行测试。 支持设置请求的响应状态码和响应体。 支持配置 <code>$&#123;int|min-max&#125;</code> , <code>$&#123;double|min-max|format&#125;</code> , <code>$&#123;email&#125;</code> , <code>$&#123;phone&#125;</code> , <code>$&#123;zh|min-max&#125;</code> , <code>$&#123;list|[arg1,arg2...]&#125;</code> , <code>$&#123;array|item|length&#125;</code> 等占位符自动生成数据。</p> 
<blockquote> 
 <p>具体使用参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshenyu.apache.org%2Fzh%2Fdocs%2Fplugin-center%2Fmock%2Fmock-plugin" target="_blank">https://shenyu.apache.org/zh/docs/plugin-center/mock/mock-plugin</a></p> 
</blockquote> 
<p>用户也可以自定义开发其他占位符：</p> 
<blockquote> 
 <p>具体开发：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshenyu.apache.org%2Fzh%2Fdocs%2Fdeveloper%2Fspi%2Fcustom-mock-generator" target="_blank">https://shenyu.apache.org/zh/docs/developer/spi/custom-mock-generator</a></p> 
</blockquote> 
<h4>response 插件中自定义输出结果</h4> 
<p>ShenYu代码 :</p> 
<pre><code class="language-java">@Bean
    public ShenyuPlugin responsePlugin(final ObjectProvider<List<MessageWriter>> httpWriter) &#123;
        Map<String, MessageWriter> writerMap = new LinkedHashMap<>();
        List<MessageWriter> writerList = httpWriter.getIfAvailable(ArrayList::new);
        for (MessageWriter writer : writerList) &#123;
            List<String> supportTypes = writer.supportTypes();
            for (String type : supportTypes) &#123;
                writerMap.put(type, writer);
            &#125;
        &#125;
        return new ResponsePlugin(writerMap);
    &#125;
</code></pre> 
<p>用户自定实现 ：rg.apache.shenyu.plugin.response.strategy.MessageWriter</p> 
<pre><code class="language-java">/**
 * The interface Message writer.
 */
public interface MessageWriter &#123;

    /**
     * Write with exchange and shenyu plugin chain.
     *
     * @param exchange exchange the current server exchange
     * @param chain provides a way to delegate to the next filter
     * @return &#123;@code Mono<Void>&#125; to indicate when request processing is complete
     */
    Mono<Void> writeWith(ServerWebExchange exchange, ShenyuPluginChain chain);

    /**
     * Support type list.
     *
     * @return the list
     */
    List<String> supportTypes();
&#125;
</code></pre> 
<h3>注册中心</h3> 
<p>ShenYu的注册中心的目的是将网关的实例暴露出去,以便支持ShenYu的集群功能。可以使用shenyu-nginx项目，也可以对接其他的负载均衡服务。</p> 
<blockquote> 
 <p>ShenYu-Nginx：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fshenyu-nginx" target="_blank">https://github.com/apache/shenyu-nginx</a></p> 
</blockquote> 
<h4>新增 Nacos的支持</h4> 
<p>使用： 在网关bootstarp的yaml新增如下配置：</p> 
<pre><code>shenyu :
  instance:
    enabled: true //设置true表示打开
    registerType: nacos //类型为nacos
    serverLists: localhost:8848
    props:
</code></pre> 
<h4>新增 Consul的支持</h4> 
<p>使用： 在网关bootstarp的yaml新增如下配置：</p> 
<pre><code>shenyu :
  instance:
    enabled: true //设置true表示打开
    registerType: consul //类型为consul
    serverLists: localhost:2379
    props:
</code></pre> 
<h4>性能优化</h4> 
<ul> 
 <li> <p>升级SpringBoot 到 2.6.8, 同时将Reactor-netty升级到 1.0.19</p> </li> 
 <li> <p>网关自定义Netty全量参数配置。满足用户的个性化配置</p> </li> 
</ul> 
<blockquote> 
 <p>具体可以参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshenyu.apache.org%2Fzh%2Fdocs%2Fuser-guide%2Fproperty-config%2Fgateway-property-config" target="_blank">https://shenyu.apache.org/zh/docs/user-guide/property-config/gateway-property-config</a></p> 
</blockquote> 
<h4>新增匹配缓存策略。流量匹配效率为 <code>O(1)</code>。</h4> 
<p>如何使用? 在网关的yaml文件中进行配置：</p> 
<pre><code class="language-yaml">shenyu:
  matchCache:
    enabled: true //设置为true 开启
    maxFreeMemory: 256 # //内存大小 单位M
</code></pre> 
<h4>新增自定义线共享线程池。</h4> 
<p>如何使用? 在网关的yaml文件中进行配置：</p> 
<pre><code class="language-yaml">shenyu:
 sharedPool:
   enable: true
   prefix: "shenyu-shared"
   corePoolSize: 200
   maximumPoolSize: 2000
   keepAliveTime: 60000
   maxWorkQueueMemory: 1073741824 # 1GB
   maxFreeMemory: 268435456 # 256MB
</code></pre> 
<p>原理：自定义shenyu线程池，重写队列等等。具体可以查看如下代码：</p> 
<p><img alt="image.png" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f90425f3d95446981de10a4143203b8~tplv-k3u1fbpfcp-watermark.image?" referrerpolicy="no-referrer"></p> 
<h4>管控平台</h4> 
<ul> 
 <li>数据存储新增支持 oracle 数据库。</li> 
 <li>新增API文档管理功能。</li> 
 <li>ShenYu Admin管理控制台新增日志记录。</li> 
 <li>更多....</li> 
</ul> 
<h4>重构</h4> 
<ul> 
 <li> <p>重构 spring cloud插件负载均衡。</p> </li> 
 <li> <p>重构 IpUtils 获取 ip逻辑 。</p> </li> 
 <li> <p>Zookeeper 客户端替换成 Apache Curator。</p> </li> 
 <li> <p>重构ShenYu Java Client注册逻辑。</p> </li> 
 <li> <p>更多....</p> </li> 
</ul> 
<h4>BugFix</h4> 
<ul> 
 <li>修复 divide插件空指针异常.</li> 
 <li>修复 body 体过大的异常。</li> 
 <li>修复 Java客户端注册，循环错误。</li> 
 <li>修复 Grpc客户端注册错误。</li> 
 <li>修复 加载本地插件失败的问题。</li> 
 <li>修复 Consul注册只注册1个元数据的问题。</li> 
 <li>修复 使用Websocket同步数据时候的 CSRF攻击。</li> 
 <li>修复 Admin pg脚本错误。</li> 
 <li>更多....</li> 
</ul> 
<h2>贡献者</h2> 
<p>特别感谢对 2.5.0 的支持的贡献者，排名不分顺序。</p> 
<p>dragon-zhang,renzhuyan,moremind,xiaoyu,likeguo,qinghai777,Kevin, Qicz,,yunlongn,lianjunwei,zhengpeng,Han,weihubeats,Zihao, DamonXue(Fibonacci),Luke.Z,ShawnSiao,sunshujie1990,Codd,dayu, LiuTianyou,PJ,Sixh-PrFor,ChineseTony,chuang,erdengk,hutaishi,impactCn, Jiageng,lahmxu,qifanyyy,Shawn,SongTao,zouchangfu,damonxue,Kunshuai, mango,nuo-promise,Salted,Seth,SongTaoZhuang,wklong,AhahaGe,Bigbang, Chencheng,Dongx,Ethan,haibo.duan,Haitao,huanccwang,jerbo99,Lidyaqf Liming,midnight2104,Nick-fengzl,ningminglong,Rubén,Shuaiqi,vijay wjlonger,Zhang,zhc,Zhiqiang,ZZQ</p> 
<h2>关于Apache ShenYu</h2> 
<p><img alt="image.png" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29559f1a4a974f94b83060debbebcdc3~tplv-k3u1fbpfcp-watermark.image?" referrerpolicy="no-referrer"></p> 
<p>Apache ShenYu 一款使用 Java Reactor 开发的响应式 API 网关。以其高性能，动态灵活的流量管控，热插拔，易部署等特性，开箱即用为用户提供整套全生命周期的 API 网关，包含 API 注册、服务代理、协议转换与 API 治理等功能。于2022年7月毕业成为Apache顶级项目。</p>
                                        </div>
                                      
</div>
            