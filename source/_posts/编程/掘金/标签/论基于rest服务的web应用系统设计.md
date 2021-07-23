
---
title: '论基于rest服务的web应用系统设计'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=6996'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 01:17:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=6996'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>【摘要】</strong></p>
<p>  2011年上半年，我在上海中软资源软件有限公司(ICSS)，作为项目组长参与了公司<strong>人事管理(HR)系统开发</strong>。在系统开发前，公司在信息化建设中，也已采用请假流程、薪资管理、招聘等系统，虽然较为成熟，但彼此间互相独立，业务数据无法共享。且公司各个分公司间，对HR系统使用情况也截然不同，有的分公司由于各种原因，仍然采用手工管理本应信息系统化的业务流程。公司是以软件外包业务为主，所以人力资源管理系统在公司信息化建设中的地位至关重要。这次开发的HR系统，将整合现有的业务系统，在整个公司内部推行使用，以解决信息孤岛带来的效率低下问题。为了以后的扩展需要，保证在业务和空间尽可能大的扩展性。因此，经过研讨，决定采用REST Web服务方式实现系统应用层。本文将就HR系统开发过程，描述一下对REST服务的使用和认识的体会。</p>
<p><strong>【</strong> <strong>正文</strong> <strong>】</strong></p>
<p>  上海中软HR管理系统整体采用基于B/S的三层架构设计。</p>
<p>  我做为项目组长参与系统需求分析至测试和部署的整个过程，直接向IT部门总监汇报。负责沟通需求，建立项目组，确定系统架构风格和技术实现方案。预定开发周期为120天，系统部署后有两个月的试运行期，项目组人数在5-10人间变动。由于项目开发资源（比如时间）紧张，公司HR系统业务逻辑复杂，旧系统改进与新需求交织，项目组对业务并不熟悉，难以在一开始预估将所有业务移植到新系统的时间。因此，在开发模型选择上，采用螺旋式增量开发。首先不必追求大而全，在开发完系统基本框架基础上，优先移植最亟待改进的业务。经与领导和HR部门沟通研究， 递交了系统准备实现的功能列表，按不同实现优先级排列，标记为P1的功能优先级最高，必须实现。标记为P2/P3/P4的功能优先级依次降低，必要时可以根据资源情况需要进行裁剪。</p>
<p>  在开发技术的选择上，由于本公司业务以微软外包为主，公司的开发人员大都熟悉一项或多项微软开发技术，作为微软公司合作伙伴可以低成本获取软件开发和管理工具，方便地获取技术支持。 所以决定该系统采用微软技术：表示层基于ASP.NET 4.0； 中间业务层采用REST服务实现，基于WCF(Windows Communication Foundation) 4.0; 数据访问层基于微软的ORM构件-AEF(ADO.Net Entity Framework) 4.0。在构件的选择上，尽可能降低开发工作量，提高效率，力求避免把主要精力放在通用的技术细节，而是放在业务逻辑的研究和实现上。</p>
<p>  系统部署共有三台服务器：两台Web服务器Windows Server 2008 + IIS 7.5， 分别运行系统网站及REST服务；一台数据库服务器 Windows Server 2008 + SQL Server 2008。经过试运行，于7月份投入正式使用。目前系统状况良好，经运行评估，实现了全部必须功能，性能、安全性等质量均达到了原定设计要求。目前系统正在根据业务需要，由后续项目组做二次开发中。</p>
<p>  采用REST服务方式实现系统业务逻辑层，完全符合项目开发时考虑的两个因素：简单和灵活。传统的Internet Web服务一般基于SOAP协议，构造SOAP请求XML虽然目前.NET Framework已实现较好地封装，但不便非.Net语言调用，如客户端页面中大量采用了Ajax技术，使用JavaScript构造Soap请求非常困难。在调用服务的Web页面开发完成前，为了调试和测试服务，必须写单独的测试程序，十分不便。</p>
<p>  相比之下，而REST服务具有非常出色地灵活性。既能被服务器端面向对象语言调用，又可以直接被客户端的脚本语言调用。也很方便用浏览器和Fiddler工具进行测试。我们在项目中，并没有将REST服务单纯视为一串地址的响应，但基于HTTP协议，可以最大地利用HTTP协议的语义特性。如数据的增删改查操作对应不同Http Method(Put/Delete/Update/Get)。用户可以用相同访问服务结点(Endpoint)，根据需要，通过在请求头中设置不同的Accept-Type，获取不同形式的数据结果，比如JSON（用于Ajax)或XML(用于后台)。</p>
<p>  更好的性能和缓存支持——由于不需要构造Soap消息，请求Rest服务显然开销更小。 REST类Web服务可以利用高速缓存控制头，从而减少带宽的需求，从而REST可以改善响应时间和改进用户体验。<br>
可扩展性和无状态性——每个请求都是独立的。一旦被调用，服务器不保留任何会话，这样就可以更具响应性。通过减少事件后通讯状态的维护工作，提高了服务器的可扩展性。</p>
<p>  在为系统开发REST服务时，也遇到一些问题：</p>
<p>  一、安全性方案。并不是指REST服务安全性不足，其本身没有内置的安全支持，但所有HTTP支持安全模式和框架几乎都可以用于REST服务。真正潜在风险存在于REST灵活的使用方式上，既可以被服务器端调用又能被客户端调用，所以一开始就要明确地区分用户访问权限和系统访问权限，区分Web页面权限和REST服务权限，但有时在开发中经常混为一谈，所以要加强设计阶段这方面的文档和评估工作。</p>
<p>  二、服务接口规范性。REST服务基于URI地址访问，有非常强的语义性，服务接口的每个操作都基于一个URI模板。在实际业务中，功能类似的操作被做成多个重载，随之重载的增多，URI模板如何约定，如何扩展便成为一个规范性问题。开始时，对此未予以足够重视，在多人开发服务，以致一些服务操作语义产生了混乱，影响了理解和正确使用。后来，又额外花费时间资源统一了规定了操作Uri格式。这一方面，源于业内尚无明确的标准，更重要是，应该从设计时就全面考虑将来如果需要重载等功能扩展，URI模板的语义扩展方式。还有一些其他的规范问题，诸如一些操作包括增删改查中的一种以上的数据操作，Http Method如何定义，也应该一并考虑。</p>
<p>  三、WCF REST自身限制。WCF从3.0发展到4.0，已经是较为成熟。而WCF的REST构件，则是全新的技术，WCF作为.NET平台Web Service的替代者，无论在开发还是管理上，都极大的灵活性。而WCF REST的灵活体现在开发和使用上，在管理维护情况下，WCF REST服务接口操作未提供如WCF一样的灵活的配置功能，URI模板等元素必须在代码中设置，消息格式虽然可以根据客户端请求输出，但不能在配置文件中设置。</p>
<p>  总的来说，虽然REST服务仍然在发展中，经验与技术还有很大进步空间。但毫无疑问，基于REST服务的WEB应用程序拥有很多优势，未在在WEB系统，将有更光明的应用前景。（2259字）</p></div>  
</div>
            