
---
title: 'Hyperf 2.2 版发布！_ 企业级的渐进式 PHP 协程框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-eae3b4b3dd0111dc8683d296dd424e2e7c3.JPEG'
author: 开源中国
comments: false
date: Mon, 19 Jul 2021 14:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-eae3b4b3dd0111dc8683d296dd424e2e7c3.JPEG'
---

<div>   
<div class="content">
                                                                    
                                                        <h1>Hyperf 2.2 版本发布!</h1> 
<h2>前言</h2> 
<p>首先感谢所有 Hyperf 的支持者，从发布至今两年的时间里，我们坚持每周发布一个小版本，截止至今已经发布了超过 106 个版本，这是 Hyperf 团队传达对用户坚持和负责任精神最直接的一种方式，我们用行动来说明一切，往后我们仍将一如既往地继续保持 Hyperf 的迭代与维护。</p> 
<p>同时我们也很荣幸看到越来越多的公司选择了 Hyperf 作为公司项目的框架来使用，并反哺了很多的 Pull Request 和 Bugfixs 给 Hyperf，当前 Hyperf 的 Contributors 已超 200 人，感谢大家一起共造了生态的繁荣，我们必定不负众望！</p> 
<h2>Thanks ALL</h2> 
<p><img alt="Thanks All Contributors" src="https://oscimg.oschina.net/oscnet/up-eae3b4b3dd0111dc8683d296dd424e2e7c3.JPEG" referrerpolicy="no-referrer"></p> 
<p>在持续迭代的过程中，我们又产生了一些新的思路。我们对这些思路进行迭代、验证，并最终沉淀到了 2.2 版本中，今天很荣幸向大家公布，Hyperf 2.2 版本发布！</p> 
<h2>主要功能迭代</h2> 
<h3>DI 底层实现重构</h3> 
<p>在 2.0-2.1 版本时，为了实现 AOP 作用于非 DI 管理的对象（如 <code>new</code> 关键词实例化的对象时），底层实现采用了<code>BetterReflection</code> 组件来实现相关功能，带来新的编程体验的同时，也还是存在一些此前未攻克的问题，如下:</p> 
<ul> 
 <li>无扫描缓存时项目启动很慢</li> 
 <li>特殊场景下 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhyperf.wiki%2F2.1%2F%23%2Fzh-cn%2Fquick-start%2Fquestions%3Fid%3D%25e5%25b8%25b8%25e8%25a7%2581%25e9%2597%25ae%25e9%25a2%2598" target="_blank">Inject 和 Value 不生效</a></li> 
 <li><code>BetterReflection</code>尚未支持 PHP 8 (截止发版时)</li> 
</ul> 
<p>在新的版本里，我们弃用了 <code>BetterReflection</code> 的应用，采用了 <code>子进程扫描的方式</code> 来解决此前的问题，<strong>以上这些痛点，我们全部解决了~</strong></p> 
<p><strong>用正向的角度来描述这个功能的变更</strong>:</p> 
<ul> 
 <li>无缓存下，启动时间缩减一个数量级，以笔者所在公司的某个巨型项目为例，原启动时间长达 5分钟，新版本只需 10秒！</li> 
 <li>丰富了 <code>Inject</code> 注解注入的适用场景，但可惜仍有一种情况下无效（父类 <code>private</code> 属性注入时失效，与此前版本表现一致），我们会继续努力攻克该场景的实现</li> 
 <li>支持 <code>PHP 8</code> 及 <code>Attributes</code> 原生注解特性</li> 
</ul> 
<p>简而言之，DI 组件作为 Hyperf 的核心组件之一，现在已经达到了一个全新的阶段，创新与实用值满格~</p> 
<h3>支持 PHP 8</h3> 
<p>Hyperf 2.2 各组件已经适配 <code>PHP 8</code>，注解亦兼容 <code>PHP 8</code> 的 <code>Attributes</code> 原生注解特性。</p> 
<pre><code class="language-php"><?php
namespace App\Controller;

#[Controller]
class IndexController
&#123;
    #[GetMapping("/test")]
    public function index()
    &#123;
        ...
    &#125;
&#125;
</code></pre> 
<p>需要注意的是，<strong>同一区域同时</strong>使用 <code>注解(Annotations)</code> 和 <code>原生注解(Attributes)</code>，底层将 <strong>忽略注解(Annotations)</strong> (即使注解不同)</p> 
<pre><code class="language-php"><?php
namespace App\Controller;

/**
 * @Controller
 * 同一区域同时使用，注解(Annotations) 无效
 */
#[Middleware(TestMiddleware::class)]
class IndexController
&#123;
    // 单独使用，可以支持
    #[Inject]
    protected StdoutLoggerInterface $logger;
    
    /**
     * 单独使用，可以支持
     * @GetMapping("/test")
     */
    public function index()
    &#123;
        ...
    &#125;
&#125;
</code></pre> 
<p>需要注意的是，框架虽然已经支持 <code>PHP8</code>，但是升级时仍需要自行确认业务代码和依赖的第三方组件是否满足 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.php.net%2Fmanual%2Fzh%2Fmigration80.incompatible.php" target="_blank">PHP 8 不兼容变更</a> 。</p> 
<h3>可重复注解</h3> 
<p>在之前版本中，同一区域相同<code>Annotation</code> 无法重复使用:</p> 
<pre><code class="language-php">/**
 * @AutoController()
 * @Middleware(FooMiddleware::class)
 * @Middleware(BarMiddleware::class)
 * 重复 @Middleware 只有一个生效!
 */
class IndexController
&#123;
    
&#125;
</code></pre> 
<p>此前，重复使用相同注解只能通过注解嵌套方式实现:</p> 
<pre><code class="language-php">/**
 * @AutoController()
 * @Middlewares(&#123;
 *     @Middleware(FooMiddleware::class)
 *     @Middleware(BarMiddleware::class)
 * &#125;)
 * 非常繁琐，增加额外心智负担
 */
class IndexController
&#123;
    
&#125;
</code></pre> 
<p>在 2.2 中，我们实现了<strong>可重复注解</strong>:</p> 
<pre><code class="language-php"><?php
namespace App\Controller;

#[AutoController]
#[Middleware(FooMiddleware::class)]
#[Middleware(BarMiddleware::class)]
class IndexController
&#123;
    
&#125;
</code></pre> 
<p>当用户自定义的注解需要可重复时，将注解的父类更改为 <code>Hyperf\Di\Annotation\AbstractMultipleAnnotation</code> 即可，具体可参考框架 <code>Middleware</code> 注解的实现。</p> 
<h3>配置中心完全重构</h3> 
<p>在此前的版本，配置中心的实现是由各个零散的组件自行实现的，各组件的实现参差不一，都有一些细节实现的区别，各组件间的代码重合度也是非常高的，在 2.2 版本，我们 <strong>完全重构</strong> 了相关组件，增加了 <code>hyperf/config-center</code> 组件，该组件将作为配置中心的统一接入层和抽象层，通过结合其他配置中心的 Driver 组件来实现相关储存引擎的能力驱动，如 <code>hyperf/config-center</code> + <code>hyperf/config-apollo</code> 组件结合使用的方式来实现对 Apollo 配置中心的使用，其他驱动只需更换对应的驱动即可。这样的改造使我们极大的减少了驱动的代码量，现在简单几行代码几个类就能完成一个新的驱动的接入了。</p> 
<p>在升级使用时，注意相关配置文件的变更，新版本将由 <code>config/autoload/config_center.php</code> 配置文件来管控所有相关信息，初次创建该文件可通过运行 <code>php bin/hyperf.php vendor:publish hyperf/config-center</code> 命令生成。</p> 
<h3>服务治理组件重构</h3> 
<p>在此前的版本，<code>hyperf/service-governance</code> 组件跟配置中心所面临的问题也是一致的，我们在此版本也做了与配置中心类似的改变，比如通过 <code>hyperf/service-governance</code> + <code>hyperf/service-governance-nacos</code> 组件来实现 nacos 作为服务中心的使用。</p> 
<p>在升级使用时，注意相关配置文件的变更，新版本将由 <code>config/autoload/services.php</code> 配置文件来管控所有相关信息，内部结构有一定的改变，初次创建该文件可通过运行 <code>php bin/hyperf.php vendor:publish hyperf/service-governance</code> 命令生成。</p> 
<h3>Nacos 组件完全重构</h3> 
<blockquote> 
 <p><strong>重要：一定要重读该组件文档！！！</strong></p> 
</blockquote> 
<p>我们对 Nacos 组件做了 <strong>完全的重构</strong>，使该组件的代码实现、结构分层和 API 更加的合理，并对原来整合在一个组件内的配置中心逻辑、服务中心逻辑和客户端代码进行了拆分，如上面两个主要迭代功能介绍所示。</p> 
<p>具体使用到 Nacos 组件的一定要重新阅读新的文档，并根据新的文档指示来使用。</p> 
<h3>AMQP 组件连接机制重构</h3> 
<p>我们发现使用 AMQP 组件的用户非常的多，而作为一个消息队列组件，其性能速度对系统的削峰效果和消息投递/消费速度影响是非常大的，我们通过 <code>协程通道(Channel)</code> 实现了一个多路复用的机制，使该组件的消息投递性能提升了将近一倍！在性能提升的同时，还使得客户端与服务端间的连接稳定性得到了提升。</p> 
<p>该组件升级后会直接切换为新的连接机制，无需做任何调整。</p> 
<p>以下是抽取压测对比中的关键信息：</p> 
<h4>非 Confirm 模式投递</h4> 
<p>2.1 版本</p> 
<blockquote> 
 <p>连接池内最大数量设置为 10</p> 
</blockquote> 
<pre><code class="language-shell">$ ab -c 32 -n 10000 http://127.0.0.1:9501/
Requests per second:    5340.80 [#/sec] (mean)
Time per request:       5.992 [ms] (mean)
Time per request:       0.187 [ms] (mean, across all concurrent requests)
Transfer rate:          928.38 [Kbytes/sec] received
</code></pre> 
<p>2.2 版本</p> 
<blockquote> 
 <p>设置 2 个多路复用的连接</p> 
</blockquote> 
<pre><code class="language-shell">$ ab -c 32 -n 10000 -k http://127.0.0.1:9501/
Requests per second:    9101.44 [#/sec] (mean)
Time per request:       3.516 [ms] (mean)
Time per request:       0.110 [ms] (mean, across all concurrent requests)
Transfer rate:          1626.53 [Kbytes/sec] received
</code></pre> 
<h4>Confirm 模式投递</h4> 
<p>2.1 版本</p> 
<blockquote> 
 <p>连接池内最大数量设置为 10</p> 
</blockquote> 
<pre><code class="language-shell">$ ab -c 32 -n 5000 -k http://127.0.0.1:9501/ 
Requests per second:    797.73 [#/sec] (mean)
Time per request:       40.114 [ms] (mean)
Time per request:       1.254 [ms] (mean, across all concurrent requests)
Transfer rate:          142.56 [Kbytes/sec] received
</code></pre> 
<p>2.2 版本</p> 
<blockquote> 
 <p>设置 2 个多路复用的连接</p> 
</blockquote> 
<pre><code class="language-shell">$ ab -c 32 -n 5000 -k http://127.0.0.1:9501/
Requests per second:    1595.94 [#/sec] (mean)
Time per request:       20.051 [ms] (mean)
Time per request:       0.627 [ms] (mean, across all concurrent requests)
Transfer rate:          285.21 [Kbytes/sec] received
</code></pre> 
<h3>3 个 Incubator 组件毕业进入主库</h3> 
<p>自从采用 Incubator 机制来孵化组件后，产生了大量的新组件，很荣幸在 2.2 版本时，有 3 个 Incubator 组件毕业进入主库，这也意味着这些组件进入了生产可用阶段~</p> 
<p>以下为各个毕业的组件及其简介</p> 
<h4>hyperf/dag</h4> 
<p>该组件是一个轻量级有向无环图 (<strong>D</strong>irected <strong>A</strong>cyclic <strong>G</strong>raph) 任务编排库，通过该组件可以很轻松的完成任务的编排和运行。</p> 
<h4>hyperf/rpc-multiplex</h4> 
<p>该组件是一个实现多路复用的 RPC 协议连接组件，通过使用该库可以得到性能更高和连接更稳定的 RPC 功能；</p> 
<h4>hyperf/rpn</h4> 
<p>该组件是一个 逆波兰表示法 的实现组件，<code>RPN</code> 是一种是由波兰数学家扬·武卡谢维奇1920年引入的数学表达式方式，在逆波兰记法中，所有操作符置于操作数的后面，因此也被称为后缀表示法。逆波兰记法不需要括号来标识操作符的优先级。通过该组件可以完成 逆波兰表达式 的解析。</p> 
<h3>依赖升级</h3> 
<ul> 
 <li>升级<code>friendsofphp/php-cs-fixer</code>为<code>^3.0</code>;</li> 
 <li>升级<code>psr/container</code>为<code>^1.0|^2.0</code>;</li> 
 <li>升级<code>egulias/email-validator</code>为<code>^3.0</code>;</li> 
 <li>升级<code>markrogoyski/math-php</code>为<code>^2.0</code>;</li> 
 <li>升级<code>league/flysystem</code>为<code>^1.0|^2.0</code>;</li> 
</ul> 
<p>依赖项已更改</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3577" target="_blank">#3577</a> <code>domnikl/statsd</code>废弃，不再维护。作者建议改用<code>slickdeals/statsd</code>包；</li> 
</ul> 
<h3>即将弃用 API</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3636" target="_blank">#3636</a> <code>Hyperf\Utils\Resource</code>将在 <code>v2.3</code> 中被弃用，请改用<code>Hyperf\Utils\ResourceGenerator</code>；</li> 
</ul> 
<h3>变更明细</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3334" target="_blank">#3334</a> 将<code>LengthAwarePaginator::toArray()</code>的返回值更改为与<code>Paginator::toArray()</code>的一致；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3550" target="_blank">#3550</a> 从<code>kafka</code>删除了<code>broker</code>和 <code>bootstrap_server</code>，<strong>请使用</strong><code>brokers</code>和<code>bootstrap_servers</code>代替；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3580" target="_blank">#3580</a> 将切面的默认优先级更改为 0；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3582" target="_blank">#3582</a> 将 <code>AMQP</code> 的消费者标签更改为空字符串；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3634" target="_blank">#3634</a> 使用 <code>Fork Process</code> 策略替换 <code>BetterReflection</code>策略； 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3649" target="_blank">#3649</a> 在<code>hyperf/database</code>使用<code>gen:model</code>时移除了<code>roave/better-reflection</code>；</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3651" target="_blank">#3651</a> 在 <code>LazyLoader</code> 中移除了<code>roave/better-reflection</code>；</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3654" target="_blank">#3654</a> 在其他组件中移除了<code>roave/better-reflection</code>；</li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3676" target="_blank">#3676</a>使用<code>promphp/prometheus_client_php</code>代替<code>endclothing/prometheus_client_php</code>；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3694" target="_blank">#3694</a>更改<code>Hyperf\CircuitBreaker\CircuitBreakerInterface</code>为支持 <code>PHP8</code>； 
  <ul> 
   <li>改<code>CircuitBreaker::inc*Counter()</code>到<code>CircuitBreaker::incr*Counter()</code>；</li> 
   <li>更改了 <code>AbstractHandler::switch()</code>方法的类型提示；</li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3706" target="_blank">#3706</a> 在<code>PHP8</code> 中将<code>@Middlewares(&#123;@Middleware(FooMiddleware::class)&#125;)</code>的书写风格更改为<code>#[Middlewares(FooMiddleware::class)]</code>；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3715" target="_blank">#3715</a> 重构<code>nacos</code>组件，<strong>一定</strong>要重读文档；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3722" target="_blank">#3722</a> 删除了 <code>config_apollo.php</code>配置，<strong>请改用</strong><code>config_center.php</code>；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3725" target="_blank">#3725</a> 删除了 <code>config_etcd.php</code>配置，<strong>请改用</strong><code>config_center.php</code>；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3730" target="_blank">#3730</a> 从<code>kafka</code>中删除了<code>brokers</code>和<code>update_brokers</code>配置；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3733" target="_blank">#3733</a> 删除了 <code>zookeeper.php</code>配置，<strong>请改用</strong><code>config_center.php</code>；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3734" target="_blank">＃3734</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3772" target="_blank">#3772</a> 分割了<code>nacos</code>为<code>config-nacos</code>和<code>service-governance-nacos</code>；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3734" target="_blank">#3734</a> 重命名<code>nacos-sdk</code> 组件名为 <code>nacos</code>；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3737" target="_blank">#3737</a> 重构配置中心和配置驱动程序 
  <ul> 
   <li>添加<code>AbstractDriver</code>并将重复的代码并合到抽象类中</li> 
   <li>添加<code>PipeMessageInterface</code>以统一配置获取进程的消息结构</li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3817" target="_blank">#3817</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3818" target="_blank">#3818</a> 从 service-governance 组件中分离出 service-governance-consul 组件；</li> 
</ul> 
<p>更多</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fblob%2F2.2%2FCHANGELOG-2.2.md" target="_blank">其他变动</a></li> 
</ul> 
<h2>升级指南</h2> 
<p>我们提供了详尽的升级指南，请查阅官方文档 - <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.hyperf.wiki%2F2.1%2F%23%2Fzh-cn%2Fupgrade%2F2.2" target="_blank">2.2 升级指南</a></p> 
<h1>官网及交流</h1> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf" target="_blank">Github</a> 👈👈👈👈👈 点 Star 支持我们<br> <a href="https://gitee.com/hyperf/hyperf">Gitee 码云</a> 👈👈👈👈👈 点 Star 支持我们<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhyperf.io" target="_blank">Hyperf 官网</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhyperf.wiki" target="_blank">Hyperf 文档</a><br> Hyperf 交流群: 862099724（已满）<br> Hyperf 交流 2 群: 811414891（已满）<br> Hyperf 交流 3 群: 589051831<br> 钉钉群 一群: 34538367（已满）<br> 钉钉群 二群: 34488757</p>
                                        </div>
                                      
</div>
            