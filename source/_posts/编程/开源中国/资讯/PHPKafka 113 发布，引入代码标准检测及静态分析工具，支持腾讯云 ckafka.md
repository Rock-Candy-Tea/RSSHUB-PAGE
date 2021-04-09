
---
title: 'PHPKafka 1.1.3 发布，引入代码标准检测及静态分析工具，支持腾讯云 ckafka'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1461'
author: 开源中国
comments: false
date: Fri, 09 Apr 2021 10:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1461'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">PHP Kafka 客户端，支持 PHP-FPM、Swoole 环境使用。通讯协议的结构基于 Java 版本中的 JSON 文件生成，这可能是有史以来支持消息类型最多的 PHP Kafka 客户端，支持全部 50 个 API。 目前已实现消息的生成及消费。</p> 
<p style="text-align:left">龙之言官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.longlang.org%2F" target="_blank">https://www.longlang.org</a></p> 
<p style="text-align:left">增强</p> 
<p>增加代码标准检测 php-cs-fixer<br> 增加静态分析工具 phpstan<br> 在 ConsumerConfig 中增加 minBytes、maxBytes、maxWait<br> 在 ConsumerConfig 中增加 brokers。broker 现在是 brokers 的别名了<br> 增加 issue 提问模版</p> 
<h3>优化</h3> 
<p>优化异常消息文字<br> 部分消费错误时 rejoin()</p> 
<h3>修复</h3> 
<p>修复一处可能的错误<br> 修复 RangeAssignor 和 RoundRobinAssignor<br> 修复清理日志后的消费问题</p> 
<p>修复保存偏移量</p> 
<h3>下载</h3> 
<p>Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flongyan%2Fphpkafka%2Freleases%2Ftag%2Fv1.1.3" target="_blank"><span style="color:#337fe5">https://github.com/longyan/phpkafka/releases/tag/v1.1.3</span></a><br> Gitee镜像：<span style="color:#337fe5"> </span><a href="https://gitee.com/longzhiyan/phpkafka" target="_blank"><span style="color:#337fe5">https://gitee.com/longzhiyan/phpkafka</span></a></p> 
<p>有问题的小伙伴，可以加我们官方的讨论群： 116305927</p> 
<h3>致谢</h3> 
<p>PHPKafka 项目自发布以来，受到了国内外众多开发者们的支持与帮助。在这里感谢所有小伙伴们对 PHPKafka 项目的喜爱，同时特别感谢来自巴西的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fleocavalcante" target="_blank"><span style="color:#337fe5">Leo Cavalcante</span></a> 同学为项目提交的代码。</p> 
<p>希望 PHPKafka 项目在大家的共同努力下健壮成长。</p> 
<h4>关于龙之言社区：</h4> 
<p><span style="background-color:#ffffff">青岛龙之言软件有限责任公司由国内著名的 Swoole团队和 禅道团队合资成立。龙之言公司主要的使命就是弥补PHP的短板，完善PHP的生态，为中国的PHP用户提供有力的技术支持。我们的项目将主要以开源的方式来进行发布，如果您有什么好的想法，或者痛点，或者想参与到我们的开发中来，欢迎和我们联系。</span><br> <br> <span style="background-color:#ffffff">我们的联系方式： guoxinhua@swoole.com    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.longlang.org%2F" target="_blank"><span style="color:#337fe5">https://www.longlang.org</span></a></p> 
<h4>写给PHPer小伙伴们的话：</h4> 
<p><span style="background-color:#ffffff">1. 你并不孤单。全世界范围内有大量的小伙伴在使用PHP。</span><br> <span style="background-color:#ffffff">2. PHP也许是本地支持最好的语言之一。我们成立龙之言社区的目的就是加强本土化的支持。</span><br> <span style="background-color:#ffffff">3. PHP越来越严谨规范，同时又保持了灵活的特点。这方面平衡把握的很好。</span><br> <span style="background-color:#ffffff">3. PHP的执行速度越来越快，未来的应用场景会更广，不仅仅局限于web。</span><br> <span style="background-color:#ffffff">4. PHP是一门特别注重实效的编程语言。很适合精益敏捷的团队。</span><br> <span style="background-color:#ffffff">5. 空谈无用，实干成事。PHPer没有必要打口水仗。提升自己，提高自己的收入和生活品质才重要。</span><br> <span style="background-color:#ffffff">6. PHP早已经不是昔日的PHP。PHPer也应该与时俱进。好的技术、语言都应该了解涉猎，为我所用。</span><br> <br> <span style="background-color:#ffffff">New PHP，New PHPer。</span></p>
                                        </div>
                                      
</div>
            