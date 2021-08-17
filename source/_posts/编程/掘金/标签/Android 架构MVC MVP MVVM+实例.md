
---
title: 'Android 架构MVC MVP MVVM+实例'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1b8bcac475541b3ac0dbc382d85e402~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 23:24:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1b8bcac475541b3ac0dbc382d85e402~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与8月更文挑战的第8天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">前言</h1>
<p>MVC，MVP和MVVM是软件比较常用的三种软件架构，这三种架构的目的都是分离，避免将过多的逻辑全部堆积在一个类中。</p>
<p>在Android中，Activity中既有UI的相关处理逻辑，又有数据获取逻辑，从而导致Activity逻辑复杂不单一难以维护。</p>
<p>为了一个应用可以更好的维护和扩展，我们需要很好的区分相关层级，要不然以后将数据获取方式从数据库变为网络获取时，我们需要去修改整个Activity。架构使得View和数据相互独立，我们把应用分成三个不同层级，这样我们就能够单独测试相关层级，使用架构能够把大多数逻辑从Activity中移除，方便进行单元测试。</p>
<h1 data-id="heading-1">MVC是什么？</h1>
<p>MVC是模型(Model)－视图(View)－控制器(Controller)的缩写，用一种业务逻辑、数据、界面显示分离的方法组织代码。其实Android Studio创建一个项目的模式就是一个简化的mvc模式。</p>
<h2 data-id="heading-2">Android中的MVC含义</h2>
<ul>
<li><strong>Model</strong>：实体类(数据的获取、存储、数据状态变化)。</li>
<li><strong>View</strong>：布局文件</li>
<li><strong>Controller</strong>：Activity(处理数据、业务和UI)。</li>
</ul>
<h2 data-id="heading-3">工作原理</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1b8bcac475541b3ac0dbc382d85e402~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>1.View接受用户的交互请求。</li>
<li>2.View将请求转交给Controller。</li>
<li>3.Controller操作Model进行数据更新。</li>
<li>4.数据更新之后，Model通知View数据变化。</li>
<li>5.View显示更新之后的数据。</li>
</ul>
<h2 data-id="heading-4">MVC的缺点</h2>
<p>随着界面及其逻辑的复杂度不断提升，Activity类的职责不断增加，以致变得庞大臃肿。</p>
<p>为了解决MVC的缺点，MVP 框架被提出来。</p>
<h1 data-id="heading-5">MVP是什么</h1>
<p>MVP是MVC架构的一个演化版，全称是Model-View-Presenter。将MVC中的V和C结合生成MVP中的V，引入新的伙伴Presenter。</p>
<h2 data-id="heading-6">Android中的MVP含义</h2>
<ul>
<li><strong>Model</strong>：实体类(数据的获取、存储、数据状态变化)。</li>
<li><strong>View</strong>：布局文件+Activity。</li>
<li><strong>Presenter</strong>：中介，负责完成View与Model间的交互和业务逻辑。</li>
</ul>
<h2 data-id="heading-7">工作原理</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cda7a03cf0ed4f11b4a46782d77036fe~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>1.View 接收用户交互请求</li>
<li>2.View 将请求转交给 Presenter(V调用P接口)</li>
<li>3.Presenter 操作Model进行数据更新(P调用M接口)</li>
<li>4.Model 通知Presenter数据发生变化(M调用P接口)</li>
<li>5.Presenter 更新View数据(P执行接口,V相应回调)</li>
</ul>
<h2 data-id="heading-8">MVP的优点</h2>
<ul>
<li>1.复杂的逻辑处理放在Presenter进行处理，减少了Activity的臃肿。</li>
<li>2.解耦。Model层与View层完全分离，修改V层不会影响M层，降低了耦合性。</li>
<li>3.可以将一个Presenter用于多个视图，而不需要改变Presenter的逻辑。</li>
<li>4.Presenter层与View层的交互是通过接口来进行的，便于单元测试。</li>
</ul>
<h2 data-id="heading-9">MVP的缺点</h2>
<p>维护困难。Presenter中除了业务逻辑以外，还有大量的View->Model，Model->View的手动同步逻辑，造成Presenter比较笨重，维护起来会比较困难。</p>
<h1 data-id="heading-10">MVVM是什么</h1>
<p>是 Model-View-ViewModel 的简写。MVVM与MVP的结构还是很相似的，就是<strong>将Presenter升级为ViewModel</strong>。在MVVM中，View层和Model层进行了<strong>双向绑定</strong>(即Data Binding)，所以Model数据的更改会表现在View上，反之亦然。ViewModel就是用来根据具体情况处理View或Model的变化。</p>
<h2 data-id="heading-11">Android中的MVVM含义</h2>
<ul>
<li><strong>Model</strong>：实体类(数据的获取、存储、数据状态变化)。</li>
<li><strong>View</strong>：布局文件+Activity。</li>
<li><strong>ViewModel</strong>： 关联层，将Model和View进行绑定，Model或View更改时，实时刷新对方。</li>
</ul>
<p>工作原理</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cb68983949e49fe93a6d31aa8c2bcd9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>1.View 接收用户交互请求</li>
<li>2.View 将请求转交给ViewModel</li>
<li>3.ViewModel 操作Model数据更新</li>
<li>4.Model 更新完数据，通知ViewModel数据发生变化</li>
<li>5.ViewModel 更新View数据</li>
</ul>
<p><strong>View/Model的变动，只要改其中一方，另一方都能够及时更新到</strong></p>
<h2 data-id="heading-12">MVVM的优点</h2>
<ul>
<li>1.提高可维护性。Data Binding可以实现双向的交互，使得视图和控制层之间的耦合程度进一步降低，分离更为彻底，同时减轻了Activity的压力。</li>
<li>2.简化测试。因为同步逻辑是交由Binder做的，View跟着Model同时变更，所以只需要保证Model的正确性，View就正确。大大减少了对View同步更新的测试。</li>
<li>3.ViewModle易于单元测试。</li>
</ul>
<h2 data-id="heading-13">MVVM的缺点</h2>
<ul>
<li>1.对于简单的项目，使用MVVM有点大材小用。</li>
<li>2.对于过大的项目，数据绑定会导致内存开销大，影响性能。</li>
<li>3.ViewModel和View的绑定，使页面异常追踪变得不方便。有可能是View出错，也有可能是ViewModel的业务逻辑有问题，也有可能是Model的数据出错。</li>
</ul>
<h1 data-id="heading-14">MVP和MVC的最大区别</h1>
<p>在MVP中View并不直接使用Model，它们之间的通信是通过Presenter 来进行的，所有的交互都发生在Presenter内部，而在MVC中View直接从Model中读取数据而不是通过 Controller。</p>
<h1 data-id="heading-15">如何选取框架</h1>
<p>本来是要每个模式写一个适用场景，最后想想每个人都有自己的理解，别被他人束缚了。</p>
<p>一句话：适合自己的才是最好的！</p>
<h1 data-id="heading-16">实例</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b348fdeaa64347d1861efca4a68513df~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
就这么一个界面咱通过MVC、MVP、MVVM分别搭建一下。</p>
<h2 data-id="heading-17">MVC实例</h2>
<h3 data-id="heading-18">代码结构</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd08370c695d4cc6ba77a01aa46e7f7b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">1.在layout创建一个布局文件</h3>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-comment"><!--缩减版--></span>
    <span class="hljs-tag"><<span class="hljs-name">LinearLayout</span>
        <span class="hljs-attr">...</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">EditText</span>
            <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/et_account"</span>
            <span class="hljs-attr">...</span>/></span>
    <span class="hljs-tag"></<span class="hljs-name">LinearLayout</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">LinearLayout</span>
        <span class="hljs-attr">...</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">EditText</span>
            <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/et_password"</span>
            <span class="hljs-attr">...</span>/></span>
    <span class="hljs-tag"></<span class="hljs-name">LinearLayout</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Button</span>
        <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/btn_login"</span>
        <span class="hljs-attr">...</span>/></span>
    <span class="hljs-tag"><<span class="hljs-name">Button</span>
        <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/btn_back"</span>
        <span class="hljs-attr">...</span>/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">2.实体类(User)</h3>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">User</span> </span>&#123;
    <span class="hljs-keyword">private</span> String name;
    <span class="hljs-keyword">private</span> String password;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">User</span><span class="hljs-params">()</span> </span>&#123;&#125;
    <span class="hljs-comment">//set or get ...</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">User</span><span class="hljs-params">(String name, String password)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.name = name;
        <span class="hljs-keyword">this</span>.password = password;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">3.MVCLoginActivity</h3>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">//用户点击事件</span>
mvcBinding.mcvLogin.btnLogin.setOnClickListener(<span class="hljs-keyword">new</span> View.OnClickListener() &#123;
            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onClick</span><span class="hljs-params">(View v)</span> </span>&#123;
                user.setName(mvcBinding.mcvLogin.etAccount.getText().toString());
                user.setPassword(mvcBinding.mcvLogin.etPassword.getText().toString());
                login(user);
            &#125;
&#125;);
<span class="hljs-comment">//逻辑处理</span>
<span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">login</span><span class="hljs-params">(User user)</span></span>&#123;
        <span class="hljs-keyword">if</span>(!user.getName().isEmpty()&&!user.getPassword().isEmpty())&#123;
            <span class="hljs-keyword">if</span>(user.getName().equals(<span class="hljs-string">"scc001"</span>)&&user.getPassword().equals(<span class="hljs-string">"111111"</span>))
            &#123;
                Toast.makeText(<span class="hljs-keyword">this</span>,<span class="hljs-string">"登录成功"</span>,Toast.LENGTH_SHORT).show();
            &#125;<span class="hljs-keyword">else</span>&#123;
                Toast.makeText(<span class="hljs-keyword">this</span>,<span class="hljs-string">"登录失败"</span>,Toast.LENGTH_SHORT).show();
            &#125;
        &#125;<span class="hljs-keyword">else</span> &#123;
            Toast.makeText(<span class="hljs-keyword">this</span>,<span class="hljs-string">"登录失败"</span>,Toast.LENGTH_SHORT).show();
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">MVP实例</h2>
<h3 data-id="heading-23">代码结构</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/661d320485dd49f3a5e3df0ee41ca485~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-24">1.Model层</h3>
<p><strong>实体类bean</strong>，同MVC中的User类，就不贴代码浪费大家时间了。</p>
<p><strong>Model层所要执行的业务逻辑</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
  * 功能：接口，表示Model层所要执行的业务逻辑
  */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">LoginModel</span> </span>&#123;
    <span class="hljs-comment">//User实体类；OnLoginFinishedListener presenter业务逻辑的返回结果</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">login</span><span class="hljs-params">(User user, OnLoginFinishedListener listener)</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>实现类(实现LoginModel接口)</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
  * 功能：实现Model层逻辑
  */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LoginModelImpl</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">LoginModel</span> </span>&#123;
    <span class="hljs-comment">//第4步：验证帐号密码</span>
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">login</span><span class="hljs-params">(User user, OnLoginFinishedListener listener)</span> </span>&#123;
        <span class="hljs-keyword">if</span>(user.getName().isEmpty()||!user.getName().equals(<span class="hljs-string">"scc001"</span>))&#123;
            <span class="hljs-comment">//第5步：Model层里面回调Presenter层listener</span>
            listener.onUserNameError();
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(user.getPassword().isEmpty()||!user.getPassword().equals(<span class="hljs-string">"111111"</span>))&#123;
            <span class="hljs-comment">//第5步：Model层里面回调Presenter层listener</span>
            listener.onPasswordError();
        &#125;<span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">//第5步：Model层里面回调Presenter层listener</span>
            listener.onSuccess();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">2.Presenter层</h3>
<p><strong>当Model层得到请求的结果，回调Presenter层，让Presenter层调用View层的接口方法。</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
  * 功能：当Model层得到请求的结果，回调Presenter层，让Presenter层调用View层的接口方法。
  */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">OnLoginFinishedListener</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">onUserNameError</span><span class="hljs-params">()</span></span>;

    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">onPasswordError</span><span class="hljs-params">()</span></span>;

    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">onSuccess</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>完成登录的验证，以及销毁当前View。</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
  * 功能：登录的Presenter的接口，实现类为LoginPresenterImpl，
  * 完成登录的验证，以及销毁当前View。
  */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">LoginPresenter</span> </span>&#123;
    <span class="hljs-comment">//完成登录的验证</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">verifyData</span><span class="hljs-params">(User user)</span></span>;
    <span class="hljs-comment">//销毁当前View</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">onDestroy</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Presenter实现类，引入 LoginModel(model)和LoginView(view)的引用</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
  * 功能：实现类，引入 LoginModel(model)和LoginView(view)的引用
  */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LoginPresenterImpl</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">OnLoginFinishedListener</span>, <span class="hljs-title">LoginPresenter</span> </span>&#123;
    <span class="hljs-comment">//View层接口</span>
    <span class="hljs-keyword">private</span> LoginView loginView;
    <span class="hljs-comment">//Model层接口</span>
    <span class="hljs-keyword">private</span> LoginModel loginModel;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">LoginPresenterImpl</span><span class="hljs-params">(LoginView loginView)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.loginView = loginView;
        <span class="hljs-keyword">this</span>.loginModel = <span class="hljs-keyword">new</span> LoginModelImpl();
    &#125;
    <span class="hljs-comment">//第6步：通过OnLoginFinishedListener验证结果回传到Presenter层</span>
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onUserNameError</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">if</span> (loginView != <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-comment">//第7步：通过loginView回传到View层</span>
            loginView.setUserNameError();
            loginView.hideProgress();
        &#125;

    &#125;
    <span class="hljs-comment">//第6步：通过OnLoginFinishedListener验证结果回传到Presenter层</span>
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onPasswordError</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">if</span> (loginView != <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-comment">//第7步：通过loginView回传到View层</span>
            loginView.setPasswordError();
            loginView.hideProgress();
        &#125;
    &#125;
    <span class="hljs-comment">//第6步：通过OnLoginFinishedListener验证结果回传到Presenter层</span>
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onSuccess</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">if</span> (loginView != <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-comment">//第7步：通过loginView回传到View层</span>
            loginView.success();
            loginView.hideProgress();
        &#125;
    &#125;


    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">verifyData</span><span class="hljs-params">(User user)</span> </span>&#123;
        <span class="hljs-keyword">if</span> (loginView != <span class="hljs-keyword">null</span>) &#123;
            loginView.showProgress();
        &#125;
        <span class="hljs-comment">//第3步：调用model层LoginModel接口的login()方法</span>
        loginModel.login(user,<span class="hljs-keyword">this</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onDestroy</span><span class="hljs-params">()</span> </span>&#123;
        loginView = <span class="hljs-keyword">null</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">3.View层</h3>
<p><strong>布局文件同MVC中的View层</strong>，就不贴代码浪费大家时间了。</p>
<p><strong>Presenter与View交互是通过接口。</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
  * 功能：Presenter与View交互是通过接口。
  * 接口中方法的定义是根据Activity用户交互需要展示的控件确定的。
  */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">LoginView</span> </span>&#123;
    <span class="hljs-comment">//login是个耗时操作,加载中(一般用ProgressBar)</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">showProgress</span><span class="hljs-params">()</span></span>;
    <span class="hljs-comment">//加载完成</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">hideProgress</span><span class="hljs-params">()</span></span>;
    <span class="hljs-comment">//login账号失败给出提示</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">setUserNameError</span><span class="hljs-params">()</span></span>;
    <span class="hljs-comment">//login密码失败给出提示</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">setPasswordError</span><span class="hljs-params">()</span></span>;
    <span class="hljs-comment">//login成功</span>
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">success</span><span class="hljs-params">()</span></span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>MVPLoginActivity</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
  * 功能：需要实现LoginView接口。
  */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MVPLoginActivity</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AppCompatActivity</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">LoginView</span> </span>&#123;
    LoginPresenterImpl loginPresenterImpl;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onCreate</span><span class="hljs-params">(<span class="hljs-meta">@Nullable</span> Bundle savedInstanceState)</span> </span>&#123;
        ...
        <span class="hljs-comment">//创建一个Presenter对象</span>
        loginPresenterImpl = <span class="hljs-keyword">new</span> LoginPresenterImpl(MVPLoginActivity.<span class="hljs-keyword">this</span>);
        <span class="hljs-comment">//第1步：用户点击登录</span>
        mvpBinding.mvpLogin.btnLogin.setOnClickListener(<span class="hljs-keyword">new</span> View.OnClickListener() &#123;
            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onClick</span><span class="hljs-params">(View v)</span> </span>&#123;
                User user = <span class="hljs-keyword">new</span> User();
                user.setName(mvpBinding.mvpLogin.etAccount.getText().toString());
                user.setPassword(mvpBinding.mvpLogin.etPassword.getText().toString());
                <span class="hljs-comment">//第2步：调用Presenter接口中的验证方法</span>
                loginPresenterImpl.verifyData(user);
            &#125;
        &#125;);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">showProgress</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-comment">//加载中</span>
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">hideProgress</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-comment">//加载完成</span>
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setUserNameError</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-comment">//第7步：通过loginView回传到View层</span>
        <span class="hljs-comment">//账号错误</span>
        Toast.makeText(<span class="hljs-keyword">this</span>,<span class="hljs-string">"登录失败"</span>,Toast.LENGTH_SHORT).show();
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setPasswordError</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-comment">//第7步：通过loginView回传到View层</span>
        <span class="hljs-comment">//密码错误</span>
        Toast.makeText(<span class="hljs-keyword">this</span>,<span class="hljs-string">"登录失败"</span>,Toast.LENGTH_SHORT).show();
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">success</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-comment">//第7步：通过loginView回传到View层</span>
        Toast.makeText(<span class="hljs-keyword">this</span>,<span class="hljs-string">"登录成功"</span>,Toast.LENGTH_SHORT).show();
        <span class="hljs-comment">//登录成功</span>
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onDestroy</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">super</span>.onDestroy();
        loginPresenterImpl.onDestroy();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">MVVM实例</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbe87aeed088412c9dcd23e84edcd08f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-28">1.Model层</h3>
<p><strong>实体类bean</strong>，同MVC中的User类，就不贴代码浪费大家时间了。</p>
<h3 data-id="heading-29">2.ViewModel层</h3>
<p><strong>ViewModel类</strong>，继承自ViewModel</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LoginViewModel</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">ViewModel</span> </span>&#123;
    <span class="hljs-keyword">public</span> ViewDataBinding binding;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">LoginViewModel</span><span class="hljs-params">(ViewDataBinding binding)</span></span>&#123;
        <span class="hljs-keyword">this</span>.binding = binding;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">getUser</span><span class="hljs-params">(String userName, String password, Callback callback)</span> </span>&#123;
        <span class="hljs-comment">//逻辑处理</span>
        User user = <span class="hljs-keyword">new</span> User();
        user.setPassword(<span class="hljs-string">"111111"</span>);
        <span class="hljs-keyword">if</span>(userName.isEmpty()||!userName.equals(<span class="hljs-string">"scc001"</span>))&#123;
            user.setName(<span class="hljs-string">"scc005"</span>);
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(password.isEmpty()||!password.equals(<span class="hljs-string">"111111"</span>))&#123;
            user.setName(<span class="hljs-string">"scc004"</span>);
        &#125;<span class="hljs-keyword">else</span> &#123;
            user.setName(<span class="hljs-string">"scc003"</span>);
        &#125;
        callback.onCallBack(user);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>ViewModel与View交互</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
  * 功能：ViewModel与View交互。
  */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Callback</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">onCallBack</span><span class="hljs-params">(T t)</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">3.View层</h3>
<p><strong>先看布局文件</strong>，布局文件使用了DataBinding。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><?xml version="1.0" encoding="utf-8"?></span>
<span class="hljs-tag"><<span class="hljs-name">layout</span> <span class="hljs-attr">xmlns:android</span>=<span class="hljs-string">"http://schemas.android.com/apk/res/android"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">data</span>></span>
        <span class="hljs-comment"><!--为引入的类从新起一个变量名，方便下面使用--></span>
        <span class="hljs-tag"><<span class="hljs-name">variable</span>
            <span class="hljs-attr">name</span>=<span class="hljs-string">"user"</span>
            <span class="hljs-attr">type</span>=<span class="hljs-string">"com.scc.architecture.mvvm.model.User"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">data</span>></span>
    <span class="hljs-comment"><!--删减版--></span>
    <span class="hljs-tag"><<span class="hljs-name">LinearLayout</span>
        <span class="hljs-attr">...</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">LinearLayout</span>
            <span class="hljs-attr">...</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">EditText</span>
                <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/et_account"</span>
                <span class="hljs-attr">...</span>
                <span class="hljs-attr">android:text</span>=<span class="hljs-string">"@=&#123;user.name&#125;"</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">LinearLayout</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">LinearLayout</span>
            <span class="hljs-attr">...</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">EditText</span>
                <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/et_password"</span>
                <span class="hljs-attr">...</span>
                <span class="hljs-attr">android:text</span>=<span class="hljs-string">"@=&#123;user.password&#125;"</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">LinearLayout</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">Button</span>
            <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/btn_login"</span>
            <span class="hljs-attr">...</span>/></span>
    <span class="hljs-tag"></<span class="hljs-name">LinearLayout</span>></span>
<span class="hljs-tag"></<span class="hljs-name">layout</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本来Button点击事件也想用databinding去做，后来觉得这个是MVP模式就忽略了这个知识点，感兴趣的可以自己捣鼓一下，databinding还是挺好玩的。</p>
<p><strong>MVVMLoginActivity</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MVVMLoginActivity</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AppCompatActivity</span> </span>&#123;
    <span class="hljs-keyword">private</span> LoginViewModel loginVM;
    ActivityMvvmBinding mvvmBinding;
    <span class="hljs-keyword">private</span> EditText et_account,et_password;
    <span class="hljs-keyword">private</span> Button btn_login,btn_back;
    <span class="hljs-keyword">private</span> TextView tv_title;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onCreate</span><span class="hljs-params">(<span class="hljs-meta">@Nullable</span> Bundle savedInstanceState)</span> </span>&#123;
        <span class="hljs-keyword">super</span>.onCreate(savedInstanceState);
        mvvmBinding = DataBindingUtil.setContentView(<span class="hljs-keyword">this</span>, R.layout.activity_mvvm);
        et_account =findViewById(R.id.et_account);
        et_password =findViewById(R.id.et_password);
        btn_login = findViewById(R.id.btn_login);
        tv_title = findViewById(R.id.tv_title);
        tv_title.setText(<span class="hljs-string">"MVVM"</span>);

        loginVM = <span class="hljs-keyword">new</span> LoginViewModel(mvvmBinding);
        User user = <span class="hljs-keyword">new</span> User( <span class="hljs-string">"scc001"</span>, <span class="hljs-string">"111111"</span>);
        mvvmBinding.setUser(user);<span class="hljs-comment">//设置et_account：scc001|et_password：111111</span>
        <span class="hljs-comment">//第1步：用户点击登录</span>
        btn_login.setOnClickListener(<span class="hljs-keyword">new</span> View.OnClickListener() &#123;
            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onClick</span><span class="hljs-params">(View v)</span> </span>&#123;
                login(et_account.getText().toString(),et_password.getText().toString());
            &#125;
        &#125;);
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">login</span><span class="hljs-params">(String name,String password)</span> </span>&#123;
        loginVM.getUser(name,password, <span class="hljs-keyword">new</span> Callback<User>() &#123;
            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onCallBack</span><span class="hljs-params">(User user)</span> </span>&#123;
                mvvmBinding.setUser(user);<span class="hljs-comment">//同步设置控件</span>
            &#125;
        &#125;);
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>写到这里MVC、MCP、MVVM和实例基本写完了，但是感觉自己理解的不是很好，有大佬能指点就更好了。最后，希望对你有借鉴意义。</p>
<h1 data-id="heading-31"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fgongtianci123%2Fmvc-mvp-mvvm-demo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/gongtianci123/mvc-mvp-mvvm-demo" ref="nofollow noopener noreferrer">实例传送门</a></h1></div>  
</div>
            