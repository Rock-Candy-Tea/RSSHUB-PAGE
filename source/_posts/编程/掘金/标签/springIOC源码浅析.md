
---
title: 'springIOC源码浅析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/293e44197e924247ae489e8788958437~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 18 Jun 2021 08:41:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/293e44197e924247ae489e8788958437~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>参考尚硅谷雷神视频</p>
</blockquote>
<h2 data-id="heading-0">一点思考</h2>
<p>在开始分析spring IOC的源码之前，我们有必要先理清大致的脉络，而有<strong>三个问题</strong>对脉络的构建至关重要——</p>
<ol>
<li>
<p><strong>从哪里出发</strong>：hello world~ 要想通这一点，我们需要把视角拉回<code>java web</code>，不可置否的是javaweb通过servlet组件可以实现一个完整的功能，但对于一个HTTP请求，我们处理的全过程包含<code>接收请求，处理请求，返回请求</code>，在这其中只有处理请求的<code>核心业务逻辑是需要我们去完成</code>的.</p>
<p>而接收请求，返回请求是所有业务场景依托的通用部分，它们完成了报文的<code>解复用，解析，封装</code>，这里的任何一项留给程序员去做，都足以<code>让人头皮发麻</code>。而框架的实现者深知这一点，把最复杂，但也最通用的部分提取了出来。</p>
<blockquote>
<p>如果我们想运行任何一个项目，一句简单的helloworld就能像点睛之笔一般让项目枯木逢春。</p>
</blockquote>
<p>转念去想，我们学习任何知识似乎都只需要一句的hello world，看来所有的框架都认为我们不怎么聪明的亚子。。</p>
</li>
<li>
<p><strong>以什么为参考</strong>：ioc容器的功能是创建并管理对象，所以对象什么时候被创建，什么时候被初始化是核心。</p>
</li>
<li>
<p><strong>解析的技巧</strong>：让人诟病的框架通常差的千奇百怪，但往往一个优秀的框架在各个方面都无可挑剔，比如<code>注释，名称</code>。</p>
<p>这些<strong>路标</strong>能够指引更高效的前行。</p>
<hr>
</li>
</ol>
<h2 data-id="heading-1">准备工作</h2>
<p>我们首先在spring的配置文件中配置了<strong>两个bean对象</strong>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/293e44197e924247ae489e8788958437~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508101816973" loading="lazy" referrerpolicy="no-referrer"></p>
<p>并通过简易的helloworld类中<strong>打断点观察源码</strong>的运行轨迹——</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0004607939b84b188e88a821bd9e9699~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508102002505" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果我们直接运行项目，会在控制台观察到这些信息：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34f883a5f8b642b79e6d0e02a62172d6~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508102357843" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来我们为创建IOC容器这一步打断点，看看会发生什么——</p>
<h2 data-id="heading-2">第一站</h2>
<blockquote>
<p>所有的故事都从这一句代码开始了：ioc = new ClassPathXmlApplicationContext("classpath:applicationContext.xml");</p>
</blockquote>
<p>首先来看debug之后的版面分布：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f58429b658494e42b0341f216976e624~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508102839427" loading="lazy" referrerpolicy="no-referrer"></p>
<p>核心的逻辑都在创建IOC容器的过程中完成，我们F5进去瞅瞅：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cac2e2079b74298bd2330f6eca0a2a7~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508103054925" loading="lazy" referrerpolicy="no-referrer"></p>
<p>显然，这是在做类加载相关的事情，F6继续：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5337ef7ce2af48db81072c2f74b6ea9f~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508103210061" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在构造方法中又调用了另一个构造方法，有趣的是不论构造方法怎样重构，最终调用的都是这一句，看来它就是核心啦，贴出来看看——</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48fe38cee93d461e93f30d5046207e1a~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508103417772" loading="lazy" referrerpolicy="no-referrer"></p>
<p>显然，配置文件的路径被作为一个<strong>String数组</strong>传入，refresh是个布尔值，它是之后的核心，parent就是老生常谈。</p>
<p>接下来解析xml——</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff928a6f6349463d88bd94a8010f9899~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508103951949" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这一步无非是框架对于XML文件的解析，XML文件中的信息都是String类型的，显然需要将它们提取出来还原为真实的数据类型。但这不是我们的重点，先过咯：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/810ec2c0da704aff84c94263bfd69269~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508104315170" loading="lazy" referrerpolicy="no-referrer"></p>
<p>进入到refresh方法，映入眼帘的是复杂但有迹可循的方法，从这里开始，我们已经揭开了它的第一层面纱，开始第二站</p>
<h2 data-id="heading-3">第二站</h2>
<p>refresh方法起手就是一个同步锁，这样能够保证IOC容器只会被创建一次，继续——</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce90b1c8d1a74eb7b255fd784bf557a3~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508104811500" loading="lazy" referrerpolicy="no-referrer"></p>
<p>放过这一句后，控制台打印出了<strong>正在欲刷新ApplicationContext的信息</strong>，不是我们核心关注点，next-></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38826454a68b4049a3bcb9c6f3aa876f~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508105131661" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这一步直观的看，<strong>刷新内部bean工厂创建出子类ConfigurableListableBeanFactory</strong>，来看下BeanFactory的顶层设计：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7cefe9f3824494eaa8654c7833b2313~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508105727464" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看来ConfigurableListableBeanFactory的地位不高，它的祖爷爷<strong>BeanFactory才是万恶之源</strong>，可以看出，它独有的两个方法一个用于<strong>返回遍历bean名称的迭代器</strong>，一个是不知道有啥用的<strong>冻结配置</strong>(你只读的，我怎么改...)。</p>
<p>当我们放过这句后，控制台表示我有话说：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f53f7d6e1d84a29963c4106d7b9bf37~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508110312292" loading="lazy" referrerpolicy="no-referrer"></p>
<p>也就是说，它实现的是<strong>解析XML配置文件的Bean定义，并加载到一个容器中</strong>那加载到哪里呢？ConfigurableListableBeanFactory？我们一看便知：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/203d4b8e672e4896adc9b09668e7115d~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508111122589" loading="lazy" referrerpolicy="no-referrer"></p>
<p>IOC容器读取XML中的配置到Bean工厂中以待使用，更具体的说，它<code>将Bean对象的定义放入了旗下的两个Map</code>中，徐徐图之：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc6c5bf0631348fbbb427d594c85cd78~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508111658655" loading="lazy" referrerpolicy="no-referrer"></p>
<p>见名知意，准备Bean工厂，放过后控制台，变量没有任何表示，next-></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/219b74ad5f7846a1902273bbe1b1713c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508111908977" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来是这个后置处理器的专场，但控制台，变量并没有发生变化，显然并不核心，我们简要的说明他们的功能——</p>
<p>IOC容器的核心功能是创建并管理Bean对象，但它的功能却不仅包含这个，它有不同类型的bean，它还要支撑框架自身的功能，而后置处理器就是做这个事情的。下一步咯：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47622bd40fa54160a63446ad1d5f03f8~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508112239897" loading="lazy" referrerpolicy="no-referrer"></p>
<p>初始化消息源？其实这一步是用于支持<strong>国际化功能</strong>的，但它在spring MVC才会一展身手，这里还不是它出场的时机，下一步——</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4370a2b5fea462e96c842d6966b7e15~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508112447315" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里<strong>初始化了事件的转化器</strong>，看不懂，也不属于核心，过：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1406f653c8734f73a600ed2274571b5f~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508112616745" loading="lazy" referrerpolicy="no-referrer"></p>
<p>留给子类实现？妙，起码暂时不用我关心了嘿嘿，下一个——</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56d738400a2946b09470eba387b5223b~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508112735726" loading="lazy" referrerpolicy="no-referrer"></p>
<p>初始化所有不是懒加载(饿汉模式，即<strong>容器启动以后，对象就会被创建</strong>)的<strong>单例对象</strong>。放过试试-》</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1abd8d355b0746e1b1473310fa95e59f~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508120936682" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里初始化了所有的单实例bean对象，终于到了最核心的部分，我们的第三步就从这里开始吧——</p>
<h2 data-id="heading-4">第三步</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c24c5ecef7cf4502a45cc77e2c888bd2~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508121322991" loading="lazy" referrerpolicy="no-referrer"></p>
<p>值得一提的是，这个方式隶属于<code>AbstractApplicationContext</code>,它是<code>ConfigurableApplicationContext</code>的实现类，将<code>ConfigurableListableBeanFactory</code>(我们刚才创建的Bean工厂)作为参数传入。</p>
<p>在刚开始的部分<strong>初始化类型转换服务</strong>，不是核心部分，继续-》</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ec21f15c7fc467faeafaa1381f0b12c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508122420754" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这一步就是在为解析做准备了，那下一步自然就是需要解析的部分：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/355be0bd4aa240d4af23b9b7fdea2b2d~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508122755207" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于我们没有需要Autowire的部分，所以这一步可以直接过啦——</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d34511dcf59b46279fdb635b017b7f1f~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508122955688" loading="lazy" referrerpolicy="no-referrer"></p>
<p>继续：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8d585ef317b41798840fde6ee37d605~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508123214114" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">黎明时分</h2>
<p>这里比较核心，我们不再截图，上代码：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">preInstantiateSingletons</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> BeansException </span>&#123;
        <span class="hljs-comment">//日志记录</span>
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">this</span>.logger.isDebugEnabled()) &#123;
<span class="hljs-keyword">this</span>.logger.debug(<span class="hljs-string">"Pre-instantiating singletons in "</span> + <span class="hljs-keyword">this</span>);
&#125;、
        <span class="hljs-comment">//从beanDefinitionNames中取得bean名称</span>
List<String> beanNames = <span class="hljs-keyword">new</span> ArrayList<>(<span class="hljs-keyword">this</span>.beanDefinitionNames);

        <span class="hljs-comment">//按照xml配置的bean名称创建bean对象</span>
<span class="hljs-keyword">for</span> (String beanName : beanNames) &#123;
               <span class="hljs-comment">//获取bean的配置信息</span>
RootBeanDefinition bd = getMergedLocalBeanDefinition(beanName);
                <span class="hljs-comment">//确认过代码，是我们需要的bean对象</span>
<span class="hljs-keyword">if</span> (!bd.isAbstract() && bd.isSingleton() && !bd.isLazyInit()) &#123;
                <span class="hljs-comment">//显然得到的bean名称是我们希望容器创建的普通bean，而不是factoryBean</span>
<span class="hljs-keyword">if</span> (isFactoryBean(beanName)) &#123;
<span class="hljs-keyword">final</span> FactoryBean<?> factory = (FactoryBean<?>) getBean(FACTORY_BEAN_PREFIX + beanName);
<span class="hljs-keyword">boolean</span> isEagerInit;
<span class="hljs-keyword">if</span> (System.getSecurityManager() != <span class="hljs-keyword">null</span> && factory <span class="hljs-keyword">instanceof</span> SmartFactoryBean) &#123;
isEagerInit = AccessController.doPrivileged((PrivilegedAction<Boolean>) () ->
((SmartFactoryBean<?>) factory).isEagerInit(),
getAccessControlContext());
&#125;
<span class="hljs-keyword">else</span> &#123;
isEagerInit = (factory <span class="hljs-keyword">instanceof</span> SmartFactoryBean &&
((SmartFactoryBean<?>) factory).isEagerInit());
&#125;
<span class="hljs-keyword">if</span> (isEagerInit) &#123;
getBean(beanName);
&#125;
&#125;
                <span class="hljs-comment">//我神经都蹦一块了，你就给我看这个~</span>
<span class="hljs-keyword">else</span> &#123;
getBean(beanName);
&#125;
&#125;
&#125;

<span class="hljs-comment">// Trigger post-initialization callback for all applicable beans...</span>
<span class="hljs-keyword">for</span> (String beanName : beanNames) &#123;
               <span class="hljs-comment">//通过名称开始创建对象啦</span>
Object singletonInstance = getSingleton(beanName);
<span class="hljs-keyword">if</span> (singletonInstance <span class="hljs-keyword">instanceof</span> SmartInitializingSingleton) &#123;
<span class="hljs-keyword">final</span> SmartInitializingSingleton smartSingleton = (SmartInitializingSingleton) singletonInstance;
<span class="hljs-keyword">if</span> (System.getSecurityManager() != <span class="hljs-keyword">null</span>) &#123;
AccessController.doPrivileged((PrivilegedAction<Object>) () -> &#123;
smartSingleton.afterSingletonsInstantiated();
<span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
&#125;, getAccessControlContext());
&#125;
<span class="hljs-keyword">else</span> &#123;
smartSingleton.afterSingletonsInstantiated();
&#125;
&#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来大致理理思绪：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a21de4506454a82adb705acdb7fc86d~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508124603963" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>根据bean名称获取到bean的配置信息-》从配置信息中判断是否是我们需要的bean对象-》如果是，再判断是工厂Bean还是普通Bean-》普通bean，调用getBean。</code></p>
<p>看来最终创建bean对象的就是这个getbean方法咯，F6一手：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da8368ed2d1c47978d222463ce172b9a~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508124353828" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一个bean被创建，我们来看看怎样实现的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86fbaa5147f14974aff6c986e08ac4ef~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508124938259" loading="lazy" referrerpolicy="no-referrer"></p>
<p>进去看看：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca81c5efd89e46f7b8d05f151a09ad86~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508125251963" loading="lazy" referrerpolicy="no-referrer"></p>
<p>也就是查询缓存咯，因为我们是第一次注册，显然不存在这个Bean，继续：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5d5b5bfc4e2408bbcc9ec27ceb31075~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508130650268" loading="lazy" referrerpolicy="no-referrer"></p>
<p>继续，来到了这：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32cc25b49edd4b38809b65894c702e13~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508130939660" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果存在依赖的bean，就需要首先先把这个bean创建出来，当前没有，继续：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3b045c57b5042ee9d035c2c559ea667~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508131336008" loading="lazy" referrerpolicy="no-referrer"></p>
<p>终于创建bean对象了，拼夕夕的套路也没你深^-^</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eadc98f9993d42dc85b0abe0b03f78a2~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508131922757" loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建完成啦，但是流程还没完~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/569e847c009f42e9afb81d1b5b1f6d1a~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508133621893" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这一步<strong>将创建的singtonObject加入到singletonObjects</strong>这个集合中去，而这个集合又隶属于我们刚才创建的bean工厂<code>ConfigurableListableBeanFactory</code>，也就是说我们创建的这个IOC容器是一个多集合的容器，而单例对象容器不过是它的众多集合之一。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fb9377aba8649deb512cba178bb4757~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508133336593" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到此，容器终于创建了，那我们来获取bean对象试试——</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e52438810b984de0be05c7eb4de0fa34~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508134719909" loading="lazy" referrerpolicy="no-referrer"></p>
<p>先获取ioc容器，然后调用getbean方法从单实例集合中获取指定名称的bean：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed388f1b6e3e47c4bc373707eb8ced26~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210508134941817" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">终曲</h2>
<blockquote>
<p>简述ApplicationContext与BeanFactory的区别？</p>
</blockquote>
<p>从框架设计来看，ApplicationContext是BeanFactory的子接口，BeanFactory是spring框架最底层的接口，它基于最基础，最通用，<strong>最核心的功能创建bean对象</strong>，而ApplicationContext它在BeanFactory的基础上，<strong>更多的关注容器功能的实现</strong>，也就是我们熟识的<strong>IOC,DI,AOP</strong>，再进一步说，<strong>BeanFactory是给ApplicationContext等子接口用的</strong>，而<strong>ApplicationContext直接对接开发人员</strong>，</p>
<p>另外值得一提的是，spring中应用最多的模式即为工厂模式，可以认为我们通过<strong>配置文件，注解来整合成一个制造说明说书</strong>，而底层的工厂帮我们去制造！</p>
<hr>
<blockquote>
<p>日拱一卒，功不唐捐。</p>
</blockquote></div>  
</div>
            