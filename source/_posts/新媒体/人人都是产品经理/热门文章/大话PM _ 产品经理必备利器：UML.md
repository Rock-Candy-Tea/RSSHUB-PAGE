
---
title: '大话PM _ 产品经理必备利器：UML'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/55.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 22 Jun 2018 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/55.jpg'
---

<div>   
<img data-action="zoom" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/55.jpg" referrerpolicy="no-referrer"><blockquote><p>产品经理经常与文档打交道，而如果想输出高质量的文档更离不开 UML 的帮助。本文将通过具体的需求实例来介绍产品经理必须掌握的几种 UML 图、绘制方式以及各自的使用场景。</p></blockquote>
<p>
</p><p>对于 UML 的定义及其语法在网络上已经有了详细的教程，本文不做详细的展开说明，这里用一句话来定义：</p>
<blockquote><p>UML（统一建模语言）是一种在软件设计时提供给分析师、设计师和工程师之间的通用语言。</p></blockquote>
<p>即通过面向对象的方式构建一个<strong>统一并通用</strong>的模型来解决问题，那么话说回来 UML 所构建的模型到底包括哪些内容呢？</p>
<p>我们知道，社会中各个领域都会存在或多或少的需求问题，在需求整理和分析时，可以将具有共性的需求抽象成一个基本模型。模型由其相关的对象组成，不同的对象具有不同的特征和操作。一般通过类来对对象进行实例化，其中对象的特征决定了对象的状态，而对象之间则通过消息传递来进行信息交流。</p>
<p>这样说可能有点过于抽象，举一个很简单的例子：</p>
<p>在某电商平台上，用户A需要购买电子商品，用户B需要购买生活用品，用户C需要购买生鲜食品…等等，这类需求就完全可以抽象为一个<strong>购物模型</strong>。</p>
<p>该模型中包含的两类对象分别为用户和商家，其中用户具有身份信息、购物需求等属性，而商家则具有店铺性质、商品价格等属性。同时用户可以进行加入购物车、下单等操作，商家则可以进行发布商品、发货等操作。</p>
<p>如果用户已经购买的商品，那么他的状态会变成无购买需求。在购物的整个过程中，用户和商家之间通过平台进行信息交流。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/vspZFqiTGQHggsOrBVIl.png" alt width="678" height="450" referrerpolicy="no-referrer"></p>
<p>对于产品经理，熟练掌握 UML 的作用在于：</p>
<ul>
<li>梳理产品需求及其业务流程；</li>
<li>梳理产品实现价值及其运用场景；</li>
<li>准确向设计及开发传达产品需求。</li>
</ul>
<p>也就是说，UML 给产品经理们提供了一套<strong>既能分析问题又能准确交流</strong>的图形化语言，所以说它是产品经理必备的利器之一。</p>
<p>下面本文将从产品经理工作及产品实现流程角度并结合具体案例，分别介绍几种产品经理必备的 UML 图。</p>
<h2 id="toc-1">一、用例图</h2>
<h3>1.1 定义</h3>
<p>用例图是产品经理在产品需求分析中最常用的工具图，在很多高质量的产品需求说明（PRD）中不难发现用例图的踪影。作为经常写 PRD 的产品经理都知道用例是一种描述产品需求的方法，而产品需求的根本来源还是来自用户。</p>
<p>想要快速理解用例图的含义只需要记住以下几点：</p>
<ul>
<li>Where：需求在哪里产生，即需求产生的领域；</li>
<li>Who：谁是相关的用户，即从用户角度出发；</li>
<li>What：产品/系统是什么；</li>
<li>How：如何使用这个产品/系统；</li>
<li>No Why：用户不关心产品/系统为什么可以实现。</li>
</ul>
<p>举个例子来说，小明有网购的需求，那么从小明的角度来说，他只要知道某个电商网站满足他的需求，并且知道如何使用即可，并不关心网站如何开发实现。</p>
<p>用一句话总结来说：</p>
<blockquote><p>用例图强调了从用户自身角度解决其需求的产品/系统是什么以及如何使用，不关心它的具体实现。</p></blockquote>
<p>而作为产品经理，使用用例图最大的三个优点在于：</p>
<ul>
<li>需求分析：根据不同的用例分析，产生不同的需求；</li>
<li>指导测试：在产品/系统测试时，可以根据用例生成测试用例；</li>
<li>便于沟通：产品经理与设计、开发以及客户之间可以很容易的通过用例沟通需求。</li>
</ul>
<h3>1.2 画法</h3>
<p>在学会如何画用例图之前，必须了解一个完整的用例图具体包含哪些元素：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/8nS3Y5cwGxf3pf4yCZJP.png" alt width="682" height="232" referrerpolicy="no-referrer"></p>
<p>其中关系分为四种：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/6SHFRHm3QvNTkwe5YLIS.png" alt width="687" height="166" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/gbjG6srwAFclFIJp5ydK.png" alt width="681" height="480" referrerpolicy="no-referrer"></p>
<h3>1.3 案例</h3>
<p>现在我们结合上述画法，画一个完整的电商平台案例的用例图。</p>
<p>在画图之前先分析一下需求（个别需求为了迎合上述画法而刻意说明，真实场景可能略有差异）：</p>
<ul>
<li>购物网站一般有两种用户：注册用户、非注册用户；</li>
<li>用户整个购物系统可以分为四个过程：搜索、添加购物车、下单、付款；</li>
<li>搜索又可以按价格、品牌等条件进行扩展筛选；</li>
<li>付款可以通过支付宝、微信或银行卡等方式。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/O8fdULntDVr8sLGxKVQN.png" alt width="1354" height="1134" referrerpolicy="no-referrer"></p>
<p>从用例图中可以非常清晰的看到：</p>
<ul>
<li>注册用户和非注册用户都属于用户的<strong>泛化；</strong></li>
<li>购物的四个过程组成的系统是一个电商网站的<strong>子系统；</strong></li>
<li>按条件进行搜索，这是对搜索功能的<strong>扩展</strong>，而不同的条件是筛选搜索的<strong>泛化；</strong></li>
<li>付款<strong>包含</strong>了支付宝、微信、银行卡三种方式；</li>
</ul>
<p>上图清晰并简洁的描述了用户、需求和系统主要功能之间的关系，这便是用例图最大的优点。</p>
<h2 id="toc-2">二、顺序图</h2>
<h3>2.1 定义</h3>
<p>在用例图中，我们只关心用户如何使用系统的各个功能（用例），但并不关心功能（用例）的具体实现。而顺序图通过引入时间的概念，展示了用例中各个对象的行为顺序以及对象之间的消息交互过程，所以顺序图也叫做时序图。</p>
<p>举个（不严谨的）例子：在小明网购的用例中，参与的对象有小明自己、网购平台和支付平台。那么顺序图则可以展示从网购开始到结束这段时间内，三者之间的消息传递过程。</p>
<p>同样用一句话来定义：</p>
<blockquote><p>顺序图是一种面向对象的动态图形，显示用例中参与交互的所有对象之间消息传递的时间顺序。</p></blockquote>
<p>而作为产品经理，顺序图能更加清晰的梳理业务关系及流程，保证产品需求的准确性、可实现性。</p>
<h3>2.2 画法</h3>
<p>从定义中不难发现，顺序图是以对象和时间为维度的二维图形，图形中的对象是按照时间顺序排列。</p>
<p>在了解其画法之前，先来看看顺序图中重要的元素（高级元素暂不介绍）：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/sDrbP6dJj5v4HsJSEZbt.png" alt width="698" height="245" referrerpolicy="no-referrer"></p>
<p>其中消息分为四种：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/a9YVZ9NEzMFRUTugnIWO.png" alt width="696" height="169" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/XqvV9Ky25KrhwSPKUb5W.png" alt width="681" height="417" referrerpolicy="no-referrer"></p>
<p><strong>特别注意：</strong></p>
<ul>
<li>顺序图必须是两个或两个以上对象间进行交互；</li>
<li>顺序图的阅读是从上到下、从左到右进行；</li>
<li>消息的传递代表的是责任分配，不代表数据传递。</li>
</ul>
<h3>2.3 案例</h3>
<p>结合上述画法，继续来看一个具体案例。该案例为用户在购物平台上，从挑选商品到下单最后成功支付的过程，先来分析一下需求（个别需求为了迎合上述画法而刻意说明，真实场景可能略有差异）：</p>
<ul>
<li>用户登录购物网站，并进行搜索并确认商品，最后进行下单操作；</li>
<li>创建订单后进入第三方支付平台进行支付操作；</li>
<li>支付结果会反馈给平台；</li>
<li>购物结果会反馈给用户。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/XpwTjvxezF7FjPBHsYho.png" alt width="691" height="390" referrerpolicy="no-referrer"></p>
<p>从上图可以清晰的看到随着时间变化，用户与用例中其他对象的消息交互顺序，这也为产品经理与开发之间提供了更加简洁有效的沟通方式。</p>
<h2 id="toc-3">三、活动图</h2>
<h3>3.1 定义</h3>
<p>不知道大家有没有了解或使用过泳道图，泳道图其实就是活动图的一种，只不过在泳道图中，各个活动会根据其对应的对象或系统来分隔。那么什么是活动图呢？</p>
<p>活动图与顺序图很相似，也是一种描述用例的动态图形。与顺序图不同的是，活动图强调了用例中各项活动之间的约束关系及其控制流程，说白了活动图用于展示系统中一个功能（用例）的操作步骤。</p>
<p>用一句话来定义：</p>
<blockquote><p>活动图展示了用例的具体业务与工作流程，以及各项业务之间的约束关系。</p></blockquote>
<p>作为产品经理，熟练掌握活动图有以下几个好处：</p>
<ul>
<li>分析与梳理业务流程；</li>
<li>深刻理解系统功能；</li>
<li>挖掘潜在的业务需求。</li>
</ul>
<h3>3.2 画法</h3>
<p>带泳道的活动图是产品经理必备的技能之一，在了解其画法之前，先来了解活动图中重要的元素：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/QTsHcthrJIKExNOugj07.png" alt width="731" height="211" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/bHZExyTN70HT94rXSSZw.png" alt width="739" height="739" referrerpolicy="no-referrer"></p>
<p><strong>注意：</strong></p>
<ul>
<li>活动图很像流程图，但不等同于流程图；</li>
<li>活动图强调对象的活动，顺序图强调对象及其生命周期；</li>
<li>泳道并不是必须的元素。</li>
</ul>
<h3>3.3 案例</h3>
<p>由于活动图与顺序图很相似，所以我们可以将顺序图的案例改成一个带泳道的二维活动图，其中以活动作为纵轴，以对象/系统作为横轴。</p>
<p>先来分析一下需求（个别需求为了迎合上述画法而刻意说明，真实场景可能略有差异）：</p>
<ul>
<li>用户登录有成功和失败判断；</li>
<li>下单直接购买和结算购物车两种方式；</li>
<li>不管用哪种下单方式，最后都会进入支付流程；</li>
<li>支付有成功和失败判断。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/NE6rDjVodFULjVaI7jTy.png" alt width="643" height="584" referrerpolicy="no-referrer"></p>
<p><strong>注：</strong>用户应该参与全过程，这里为了说明二维泳道图的画法，刻意去除了购物与支付流程的参与。</p>
<p>从图中可以清晰的看到，用户从登录到购物结束的整个活动过程，并能看到每个活动所对应的对象，这在业务流程梳理环节能给产品经理们提供很大的帮助。</p>
<h2 id="toc-4">四、类图</h2>
<h3>4.1 定义</h3>
<p>与顺序图、活动图这两种动态图形不同的是，类图显示的是系统/产品中的静态关系及关系。在介绍什么是类图之前提个问题，还记得本文开头对 UML 框架的说明中对类的定义吗？</p>
<p>如果记得的话，你会知道：<strong>通过类创建的类实例是对象的实例化。</strong></p>
<p>通过前三种图形的学习，我们对<strong>对象</strong>这个概念已经很熟悉了，你可以简单看成是系统/产品的参与者（可以作为使用者参与，也可以作为子系统参与）。在对象实例化成类后，参与者的特征及操作也被相应的实例化成属性和方法。</p>
<p>那么有没有一种图形，可以描述用例中不同的类的数据和方法之间的关系呢？</p>
<p>没错，那就是类图。这里给出一句话定义：</p>
<blockquote><p>类图是用于描述系统/产品结构化设计的静态图形，显示了类、类的方法、类的接口以及它们之间静态结构和关系。</p></blockquote>
<p>作为产品经理，运用类图可以理清业务概念以及它们的关系，能更加深入地剖析系统/产品业务。</p>
<h3>4.2 画法</h3>
<p>从定义中不难发现，类图需要表现各个类之间的关系。在了解其画法之前，先来看看类图中重要的元素：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/U2gT78QSqOxyTfxcn6Mv.png" alt width="684" height="326" referrerpolicy="no-referrer"></p>
<p>其中多样性示例如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/5RoiNkTmfBoX0U6DaLe0.png" alt width="683" height="165" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/NHrTMfVsFI9GozlVGnEz.png" alt width="682" height="365" referrerpolicy="no-referrer"></p>
<p><strong>注意：</strong></p>
<ul>
<li>类的操作是针对类自身，并不是操作其他类；</li>
<li>由于类图中关系复杂，一定要注意规范；</li>
<li>一个复杂的实例可以被分为多个类。</li>
</ul>
<h3>4.3 案例</h3>
<p>结合上述画法，继续来看一个具体案例，仍然是用户网购用例，先来分析一下需求（个别需求为了迎合上述画法而刻意说明，真实场景可能略有差异）：</p>
<ul>
<li>用户必须使用电脑/手机才能进行网购，也就是用户依赖于电脑/手机；</li>
<li>搜索可以按照关键字/价格/品牌等进行搜索，那么搜索可以封装成接口；</li>
<li>在整个订单中包含了订单详情，发货状态等部分；</li>
<li>可以通过支付宝/微信等方式进行支付，相当于继承了支付的所有功能。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/roMTLlyPCcKXoEak5Iyr.png" alt width="689" height="353" referrerpolicy="no-referrer"></p>
<p>从图中可以清晰的看到各个被实例化之后的对象（也就是类）之间的相互关系，既能帮助产品经理更深刻的认识整个用例系统，也能便于其与开发人员之间的沟通。</p>
<h2 id="toc-5">五、总结</h2>
<p>好了，已经将 UML 中四种产品经理最常用且最有用的四种图介绍完了，现在来总结一下各图作用以及它们的使用场景：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2018/06/WGBywEgwyC7qcMYSRSgB.png" alt width="677" height="166" referrerpolicy="no-referrer"></p>
<p>产品经理可以根据根据实际情况选取最佳的图形，那么作为产品经理该如何选取画 UML 的工具？</p>
<p>使用画图工具的意义在于提升效率，而计算效率时一定要除去学习工具的时间成本，有很多非常专业的软件学习起来比较吃力，极不推荐。又由于产品经理遇到的图形非常多，如果每种图形都使用一种工具的话，不仅切换麻烦而且兼容性、一致性都很差。</p>
<p>在这里只简单推荐几款：</p>
<ul>
<li>频繁使用、专业使用 UML ：推荐 StarUML；</li>
<li>作为辅助工具使用：Win 端 Visio，Mac 端 OmniGraffle；</li>
<li>在线协作：ProcessOn。</li>
</ul>
<p>根据个人需求酌情择优，毕竟只有适合自己的才是最好的。</p>
<p><strong>参考资料：</strong></p>
<p><a href="http://edn.embarcadero.com/article/31863">UML 实践详细经典教程</a></p>
<p><a href="http://www.uml.org.cn/oobject/OObject.asp#9">UML 基础教程</a></p>
<p> </p>
<p>本文由 @ iamxiarui 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图作者提供</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="1060852" data-author="643365" data-avatar="https://static.woshipm.com/APP_U_201802_20180228172816_4901.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">5人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602183234_7459.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602175151_6636.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602183032_8797.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602182838_6232.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602182928_9320.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            