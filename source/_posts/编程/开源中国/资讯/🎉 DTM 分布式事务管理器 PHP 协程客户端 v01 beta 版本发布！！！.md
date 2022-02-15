
---
title: '🎉 DTM 分布式事务管理器 PHP 协程客户端 v0.1 beta 版本发布！！！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cdn.learnku.com/uploads/images/202202/15/21058/zh9c3GAmYq.svg'
author: 开源中国
comments: false
date: Tue, 15 Feb 2022 12:19:00 GMT
thumbnail: 'https://cdn.learnku.com/uploads/images/202202/15/21058/zh9c3GAmYq.svg'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdtm-php%2Fdtm-client" target="_blank">https://github.com/dtm-php/dtm-client</a></p> 
<h1>介绍</h1> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackagist.org%2Fpackages%2Fdtm%2Fdtm-client" target="_blank">dtm/dtm-client</a> 是分布式事务管理器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdtm-labs%2Fdtm" target="_blank">DTM</a> 的 PHP 客户端，已支持 TCC模式、Saga、二阶段消息模式的分布式事务模式，并分别实现了与 DTM Server 以 HTTP 协议或 gRPC 协议通讯，该客户端可安全运行于 PHP-FPM 和 Swoole 协程环境中，更是对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf" target="_blank">Hyperf</a> 做了更加易用的功能支持。</p> 
<h1>关于 DTM</h1> 
<p>DTM 是一款基于 Go 语言实现的开源分布式事务管理器，提供跨语言，跨存储引擎组合事务的强大功能。DTM 优雅的解决了幂等、空补偿、悬挂等分布式事务难题，也提供了简单易用、高性能、易水平扩展的分布式事务解决方案。</p> 
<h2>亮点</h2> 
<ul> 
 <li>极易上手 
  <ul> 
   <li>零配置启动服务，提供非常简单的 HTTP 接口，极大降低上手分布式事务的难度</li> 
  </ul> </li> 
 <li>跨语言 
  <ul> 
   <li>可适合多语言栈的公司使用。方便 Go、Python、PHP、NodeJs、Ruby、C# 等各类语言使用。</li> 
  </ul> </li> 
 <li>使用简单 
  <ul> 
   <li>开发者不再担心悬挂、空补偿、幂等各类问题，首创子事务屏障技术代为处理</li> 
  </ul> </li> 
 <li>易部署、易扩展 
  <ul> 
   <li>仅依赖 MySQL/Redis，部署简单，易集群化，易水平扩展</li> 
  </ul> </li> 
 <li>多种分布式事务协议支持 
  <ul> 
   <li>TCC、SAGA、XA、二阶段消息，一站式解决多种分布式事务问题</li> 
  </ul> </li> 
</ul> 
<h2>对比</h2> 
<p>在非 Java 语言下，暂未看到除 DTM 之外的成熟的分布式事务管理器，因此这里将 DTM 和 Java 中最成熟的开源项目 Seata 做对比：</p> 
<table> 
 <thead> 
  <tr> 
   <th style="text-align:center">特性</th> 
   <th style="text-align:center">DTM</th> 
   <th style="text-align:center">SEATA</th> 
   <th style="text-align:center">备注</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="text-align:center"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdtm.pub%2Fother%2Fopensource.html%23lang" target="_blank">支持语言</a></td> 
   <td style="text-align:center"><span style="color:green">Go、C#、Java、Python、PHP...</span></td> 
   <td style="text-align:center"><span style="color:orange">Java</span></td> 
   <td style="text-align:center">DTM 可轻松接入一门新语言</td> 
  </tr> 
  <tr> 
   <td style="text-align:center"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdtm.pub%2Fother%2Fopensource.html%23store" target="_blank">存储引擎</a></td> 
   <td style="text-align:center"><span style="color:green">支持数据库、Redis、Mongo等</span></td> 
   <td style="text-align:center"><span style="color:orange">数据库</span></td> 
   <td style="text-align:center"> </td> 
  </tr> 
  <tr> 
   <td style="text-align:center"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdtm.pub%2Fother%2Fopensource.html%23exception" target="_blank">异常处理</a></td> 
   <td style="text-align:center"><span style="color:green">子事务屏障自动处理 </span></td> 
   <td style="text-align:center"><span style="color:orange">手动处理</span></td> 
   <td style="text-align:center">DTM 解决了幂等、悬挂、空补偿</td> 
  </tr> 
  <tr> 
   <td style="text-align:center"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdtm.pub%2Fother%2Fopensource.html%23saga" target="_blank">SAGA事务</a></td> 
   <td style="text-align:center"><span style="color:green">极简易用</span></td> 
   <td style="text-align:center"><span style="color:orange">复杂状态机</span></td> 
   <td style="text-align:center"> </td> 
  </tr> 
  <tr> 
   <td style="text-align:center"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdtm.pub%2Fother%2Fopensource.html%23msg" target="_blank">二阶段消息</a></td> 
   <td style="text-align:center"><span style="color:green">✓</span></td> 
   <td style="text-align:center"><span style="color:red">✗</span></td> 
   <td style="text-align:center">最简消息最终一致性架构</td> 
  </tr> 
  <tr> 
   <td style="text-align:center"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdtm.pub%2Fother%2Fopensource.html%23tcc" target="_blank">TCC事务</a></td> 
   <td style="text-align:center"><span style="color:green">✓</span></td> 
   <td style="text-align:center"><span style="color:green">✓</span></td> 
   <td style="text-align:center"> </td> 
  </tr> 
  <tr> 
   <td style="text-align:center"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdtm.pub%2Fother%2Fopensource.html%23xa" target="_blank">XA事务</a></td> 
   <td style="text-align:center"><span style="color:green">✓</span></td> 
   <td style="text-align:center"><span style="color:green">✓</span></td> 
   <td style="text-align:center"> </td> 
  </tr> 
  <tr> 
   <td style="text-align:center"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdtm.pub%2Fother%2Fopensource.html%23at" target="_blank">AT事务</a></td> 
   <td style="text-align:center"><span style="color:orange">建议使用XA</span></td> 
   <td style="text-align:center"><span style="color:green">✓</span></td> 
   <td style="text-align:center">AT 与 XA类似，但有脏回滚</td> 
  </tr> 
  <tr> 
   <td style="text-align:center"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdtm.pub%2Fother%2Fopensource.html%23multidb" target="_blank">单服务多数据源</a></td> 
   <td style="text-align:center"><span style="color:green">✓</span></td> 
   <td style="text-align:center"><span style="color:red">✗</span></td> 
   <td style="text-align:center"> </td> 
  </tr> 
  <tr> 
   <td style="text-align:center"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdtm.pub%2Fother%2Fopensource.html%23protocol" target="_blank">通信协议</a></td> 
   <td style="text-align:center">HTTP、gRPC</td> 
   <td style="text-align:center">Dubbo等协议</td> 
   <td style="text-align:center">DTM对云原生更加友好</td> 
  </tr> 
  <tr> 
   <td style="text-align:center"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdtm.pub%2Fother%2Fopensource.html%23star" target="_blank">star数量</a></td> 
   <td style="text-align:center"><img alt="github stars" src="https://cdn.learnku.com/uploads/images/202202/15/21058/zh9c3GAmYq.svg" referrerpolicy="no-referrer"></td> 
   <td style="text-align:center"><img alt="github stars" src="https://cdn.learnku.com/uploads/images/202202/15/21058/pn5f7zYuSG.svg" referrerpolicy="no-referrer"></td> 
   <td style="text-align:center">DTM 从 2021-06-04 发布 0.1版本，发展飞快</td> 
  </tr> 
 </tbody> 
</table> 
<p>从上面对比的特性来看，DTM 在许多方面都具备很大的优势。如果考虑多语言支持、多存储引擎支持，那么 DTM 毫无疑问是您的首选.</p> 
<h1>安装</h1> 
<p>通过 Composer 可以非常方便的安装 dtm-client</p> 
<pre><code class="language-bash">composer require dtm/dtm-client
</code></pre> 
<ul> 
 <li>使用时别忘了启动 DTM Server 哦</li> 
</ul> 
<h1>配置</h1> 
<h2>配置文件</h2> 
<p>如果您是在 Hyperf 框架中使用，在安装组件后，可通过下面的 <code>vendor:publish</code> 命令一件发布配置文件于 <code>./config/autoload/dtm.php</code></p> 
<pre><code class="language-bash">php bin/hyperf.php vendor:publish dtm/dtm-client
</code></pre> 
<p>如果您是在非 Hyperf 框架中使用，可复制 <code>./vendor/dtm/dtm-client/publish/dtm.php</code> 文件到对应的配置目录中。</p> 
<pre><code class="language-php">use DtmClient\\Constants\\Protocol;
use DtmClient\\Constants\\DbType;

return [
    // 客户端与 DTM Server 通讯的协议，支持 Protocol::HTTP 和 Protocol::GRPC 两种
    'protocol' => Protocol::HTTP,
    // DTM Server 的地址
    'server' => '127.0.0.1',
    // DTM Server 的端口
    'port' => [
        'http' => 36789,
        'grpc' => 36790,
    ],
    // 子事务屏障配置
    'barrier' => [
        // DB 模式下的子事务屏障配置
        'db' => [
            'type' => DbType::MySQL
        ],
        // Redis 模式下的子事务屏障配置
        'redis' => [
            // 子事务屏障记录的超时时间
            'expire_seconds' => 7 * 86400,
        ],
        // 非 Hyperf 框架下应用子事务屏障的类
        'apply' => [],
    ],
    // HTTP 协议下 Guzzle 客户端的通用配置
    'guzzle' => [
        'options' => [],
    ],
];
</code></pre> 
<h2>配置中间件</h2> 
<p>在使用之前，需要配置 <code>DtmClient\\Middleware\\DtmMiddleware</code> 中间件作为 Server 的全局中间件，该中间件支持 PSR-15 规范，可适用于各个支持该规范的的框架。<br> 在 Hyperf 中的中间件配置可参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.hyperf.wiki%2F2.2%2F%23%2Fzh-cn%2Fmiddleware%2Fmiddleware" target="_blank">Hyperf文档 - 中间件</a> 一章。</p> 
<h1>使用</h1> 
<p>dtm-client 的使用非常简单，我们提供了一个示例项目 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdtm-php%2Fdtm-sample" target="_blank">dtm-php/dtm-sample</a> 来帮助大家更好的理解和调试。<br> 在使用该组件之前，也强烈建议您先阅读 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdtm.pub%2F" target="_blank">DTM 官方文档</a>，以做更详细的了解。</p> 
<h2>TCC 模式</h2> 
<p>TCC 模式是一种非常流行的柔性事务解决方案，由 Try-Confirm-Cancel 三个单词的首字母缩写分别组成 TCC 的概念，最早是由 Pat Helland 于 2007 年发表的一篇名为《Life beyond Distributed Transactions:an Apostate’s Opinion》的论文中提出。</p> 
<h3>TCC 的 3 个阶段</h3> 
<p>Try 阶段：尝试执行，完成所有业务检查（一致性）, 预留必须业务资源（准隔离性）<br> Confirm 阶段：如果所有分支的 Try 都成功了，则走到 Confirm 阶段。Confirm 真正执行业务，不作任何业务检查，只使用 Try 阶段预留的业务资源<br> Cancel 阶段：如果所有分支的 Try 有一个失败了，则走到 Cancel 阶段。Cancel 释放 Try 阶段预留的业务资源。</p> 
<p>如果我们要进行一个类似于银行跨行转账的业务，转出（TransOut）和转入（TransIn）分别在不同的微服务里，一个成功完成的 TCC 事务典型的时序图如下：</p> 
<p><img height="600" src="https://dtm.pub/assets/tcc_normal.dea14fb3.jpg" referrerpolicy="no-referrer"></p> 
<h3>代码示例</h3> 
<p>以下展示在 Hyperf 框架中的使用方法，其它框架类似</p> 
<pre><code class="language-php"><?php
namespace App\\Controller;

use DtmClient\\TCC;
use DtmClient\\TransContext;
use Hyperf\\Di\\Annotation\\Inject;
use Hyperf\\HttpServer\\Annotation\\Controller;
use Hyperf\\HttpServer\\Annotation\\GetMapping;
use Throwable;

#[Controller(prefix: '/tcc')]
class TccController
&#123;

    protected string $serviceUri = 'http://127.0.0.1:9501';

    #[Inject]
    protected TCC $tcc;

    #[GetMapping(path: 'successCase')]
    public function successCase()
    &#123;
        try &#123;
            
            $this->tcc->globalTransaction(function (TCC $tcc) &#123;
                // 创建子事务 A 的调用数据
                $tcc->callBranch(
                    // 调用 Try 方法的参数
                    ['amount' => 30],
                    // Try 方法的 URL
                    $this->serviceUri . '/tcc/transA/try',
                    // Confirm 方法的 URL
                    $this->serviceUri . '/tcc/transA/confirm',
                    // Cancel 方法的 URL
                    $this->serviceUri . '/tcc/transA/cancel'
                );
                // 创建子事务 B 的调用数据，以此类推
                $tcc->callBranch(
                    ['amount' => 30],
                    $this->serviceUri . '/tcc/transB/try',
                    $this->serviceUri . '/tcc/transB/confirm',
                    $this->serviceUri . '/tcc/transB/cancel'
                );
            &#125;);
        &#125; catch (Throwable $e) &#123;
            var_dump($e->getMessage(), $e->getTraceAsString());
        &#125;
        // 通过 TransContext::getGid() 获得 全局事务ID 并返回
        return TransContext::getGid();
    &#125;
&#125;
</code></pre> 
<h2>Saga 模式</h2> 
<p>Saga 模式是分布式事务领域最有名气的解决方案之一，也非常流行于各大系统中，最初出现在 1987 年 由 Hector Garcaa-Molrna & Kenneth Salem 发表的论文 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cs.cornell.edu%2Fandru%2Fcs711%2F2002fa%2Freading%2Fsagas.pdf" target="_blank">SAGAS</a> 里。</p> 
<p>Saga 是一种最终一致性事务，也是一种柔性事务，又被叫做 长时间运行的事务（Long-running-transaction），Saga 是由一系列的本地事务构成。每一个本地事务在更新完数据库之后，会发布一条消息或者一个事件来触发 Saga 全局事务中的下一个本地事务的执行。如果一个本地事务因为某些业务规则无法满足而失败，Saga 会执行在这个失败的事务之前成功提交的所有事务的补偿操作。所以 Saga 模式在对比 TCC 模式时，因缺少了资源预留的步骤，往往在实现回滚逻辑时会变得更麻烦。</p> 
<h3>Saga 子事务拆分</h3> 
<p>比如我们要进行一个类似于银行跨行转账的业务，将 A 账户中的 30 元转到 B 账户，根据 Saga 事务的原理，我们将整个全局事务，拆分为以下服务：</p> 
<ul> 
 <li>转出（TransOut）服务，这里将会进行操作 A 账户扣减 30 元</li> 
 <li>转出补偿（TransOutCompensate）服务，回滚上面的转出操作，即 A 账户增加 30 元</li> 
 <li>转入（TransIn）服务，这里将会进行 B 账户增加 30 元</li> 
 <li>转出补偿（TransInCompensate）服务，回滚上面的转入操作，即 B 账户减少 30 元</li> 
</ul> 
<p>整个事务的逻辑是：</p> 
<p>执行转出成功 => 执行转入成功 => 全局事务完成</p> 
<p>如果在中间发生错误，例如转入 B 账户发生错误，则会调用已执行分支的补偿操作，即：</p> 
<p>执行转出成功 => 执行转入失败 => 执行转入补偿成功 => 执行转出补偿成功 => 全局事务回滚完成</p> 
<p>下面是一个成功完成的 SAGA 事务典型的时序图：</p> 
<p><img height="428" src="https://dtm.pub/assets/saga_normal.a2849672.jpg" referrerpolicy="no-referrer"></p> 
<h3>代码示例</h3> 
<p>以下展示在 Hyperf 框架中的使用方法，其它框架类似</p> 
<pre><code class="language-php">namespace App\\Controller;

use DtmClient\\Saga;
use DtmClient\\TransContext;
use Hyperf\\Di\\Annotation\\Inject;
use Hyperf\\HttpServer\\Annotation\\Controller;
use Hyperf\\HttpServer\\Annotation\\GetMapping;

#[Controller(prefix: '/saga')]
class SagaController
&#123;

    protected string $serviceUri = 'http://127.0.0.1:9501';
    
    #[Inject]
    protected Saga $saga;

    #[GetMapping(path: 'successCase')]
    public function successCase(): string
    &#123;
        $payload = ['amount' => 50];
        // 初始化 Saga 事务
        $this->saga->init();
        // 增加转出子事务
        $this->saga->add(
            $this->serviceUri . '/saga/transOut', 
            $this->serviceUri . '/saga/transOutCompensate', 
            $payload
        );
        // 增加转入子事务
        $this->saga->add(
            $this->serviceUri . '/saga/transIn', 
            $this->serviceUri . '/saga/transInCompensate', 
            $payload
        );
        // 提交 Saga 事务
        $this->saga->submit();
        // 通过 TransContext::getGid() 获得 全局事务ID 并返回
        return TransContext::getGid();
    &#125;
&#125;
</code></pre>
                                        </div>
                                      
</div>
            