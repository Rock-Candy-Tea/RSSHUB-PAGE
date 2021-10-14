
---
title: '小公司技术总监：我去，你竟然还不会用 final 关键字'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/1179389-9e58e956fbc6cf59.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/1179389-9e58e956fbc6cf59.png'
---

<div>   
<p>写一篇文章容易吗？太不容易了，首先，需要一个安静的环境，这一点就非常不容易。很多小伙伴的办公室都是开放式的，非常吵，况且上班时间写的话，领导就不高兴了；只能抽时间写。其次，环境有了，还要有一颗安静的心，如果心里装着其他挥之不去的事，那就糟糕了，呆坐着电脑前一整天也不会有结果。</p>
<p>我十分佩服一些同行，他们写万字长文，这在我看来，几乎不太可能完成。因为我要日更，一万字的长文，如果走原创的话，至少需要一周时间，甚至一个月的时间。</p>
<p>就如小伙伴们看到的，我写的文章大致都能在五分钟内阅读完，并且能够保证小伙伴们在阅读完学到或者温习到一些知识。这就是我的风格，通俗易懂，轻松幽默。</p>
<p>好了，又一篇我去系列的文章它来了：你竟然还不会用 final 关键字。</p>
<p>已经晚上 9 点半了，我还没有下班，因为要和小王一块修复一个 bug。我订了一份至尊披萨，和小王吃得津津有味的时候，他突然问了我一个问题：“老大，能给我详细地说说 final 关键字吗，总感觉对这个关键字的认知不够全面。”</p>
<p>一下子我的火气就来了，尽管小王问的态度很谦逊，很卑微，但我还是忍不住破口大骂：“我擦，小王，你丫的竟然不会用 final，我当初是怎么面试你进来的！”</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="200" data-height="200"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-9e58e956fbc6cf59.png" data-original-width="200" data-original-height="200" data-original-format="image/png" data-original-filesize="111915" src="https://upload-images.jianshu.io/upload_images/1179389-9e58e956fbc6cf59.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>发火归发火，我这个人还是有原则的，等十点半回到家后，我决定为小王专门写一篇文章，好好地讲一讲 final 关键字，也希望给更多的小伙伴一些帮助。</p>
<p>尽管<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Fq-dMxOXxT8N3W6ftmNWkWQ" target="_blank">继承</a>可以让我们重用现有代码，但有时处于某些原因，我们确实需要对可扩展性进行限制，final 关键字可以帮助我们做到这一点。</p>
<h3>01、final 类</h3>
<p>如果一个类使用了 final 关键字修饰，那么它就无法被继承。如果小伙伴们细心观察的话，Java 就有不少 final 类，比如说最常见的 String 类。</p>
<pre><code class="java">public final class String
    implements java.io.Serializable, Comparable<String>, CharSequence,
               Constable, ConstantDesc &#123;&#125;
</code></pre>
<p>为什么 String 类要设计成 final 的呢？原因大致有以下三个：</p>
<ul>
<li>为了实现字符串常量池</li>
<li>为了线程安全</li>
<li>为了 HashCode 的不可变性</li>
</ul>
<p>更详细的原因，可以查看我之前写的一篇<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FCRQrm5zGpqWxYL_ztk-b2Q" target="_blank">文章</a>。</p>
<p>任何尝试从 final 类继承的行为将会引发编译错误，为了验证这一点，我们来看下面这个例子，Writer 类是 final 的。</p>
<pre><code class="java">public final class Writer &#123;
    private String name;

    public String getName() &#123;
        return name;
    &#125;

    public void setName(String name) &#123;
        this.name = name;
    &#125;
&#125;
</code></pre>
<p>尝试去继承它，编译器会提示以下错误，Writer 类是 final 的，无法继承。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="758" data-height="81"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-2223c08dd3f54bbf.png" data-original-width="758" data-original-height="81" data-original-format="image/png" data-original-filesize="11192" src="https://upload-images.jianshu.io/upload_images/1179389-2223c08dd3f54bbf.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>不过，类是 final 的，并不意味着该类的对象是不可变的。</p>
<pre><code class="java">Writer writer = new Writer();
writer.setName("沉默王二");
System.out.println(writer.getName()); // 沉默王二
</code></pre>
<p>Writer 的 name 字段的默认值是 null，但可以通过 settter 方法将其更改为“沉默王二”。也就是说，如果一个类只是 final 的，那么它并不是不可变的全部条件。</p>
<p>如果，你想了解不可变类的全部真相，请查看我之前写的文章<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FwbdV9rV60AwWiiTEBYPP7g" target="_blank">这次要说不明白immutable类，我就怎么地</a>。突然发现，写系列文章真的妙啊，很多相关性的概念全部涉及到了。我真服了自己了。</p>
<p>把一个类设计成 final 的，有其安全方面的考虑，但不应该故意为之，因为把一个类定义成 final 的，意味着它没办法继承，假如这个类的一些方法存在一些问题的话，我们就无法通过重写的方式去修复它。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="255" data-height="255"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-6cb83a49fdc3fd16.png" data-original-width="255" data-original-height="255" data-original-format="image/png" data-original-filesize="38905" src="https://upload-images.jianshu.io/upload_images/1179389-6cb83a49fdc3fd16.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>02、final 方法</h3>
<p>被 final 修饰的方法不能被重写。如果我们在设计一个类的时候，认为某些方法不应该被重写，就应该把它设计成 final 的。</p>
<p>Thread 类就是一个例子，它本身不是 final 的，这意味着我们可以扩展它，但它的 <code>isAlive()</code> 方法是 final 的：</p>
<pre><code class="java">public class Thread implements Runnable &#123;
    public final native boolean isAlive();
&#125;
</code></pre>
<p>需要注意的是，该方法是一个本地（native）方法，用于确认线程是否处于活跃状态。而本地方法是由操作系统决定的，因此重写该方法并不容易实现。</p>
<p>Actor 类有一个 final 方法 <code>show()</code>：</p>
<pre><code class="java">public class Actor &#123;
    public final void show() &#123;
        
    &#125;
&#125;
</code></pre>
<p>当我们想要重写该方法的话，就会出现编译错误：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="577" data-height="132"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-b133bf4f8a773acc.png" data-original-width="577" data-original-height="132" data-original-format="image/png" data-original-filesize="15618" src="https://upload-images.jianshu.io/upload_images/1179389-b133bf4f8a773acc.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>如果一个类中的某些方法要被其他方法调用，则应考虑事被调用的方法称为 final 方法，否则，重写该方法会影响到调用方法的使用。</p>
<p>一个类是 final 的，和一个类不是 final，但它所有的方法都是 final 的，考虑一下，它们之间有什么区别？</p>
<p>我能想到的一点，就是前者不能被继承，也就是说方法无法被重写；后者呢，可以被继承，然后追加一些非 final 的方法。没毛病吧？看把我聪明的。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="265" data-height="247"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-44f9f35d1900a37d.png" data-original-width="265" data-original-height="247" data-original-format="image/png" data-original-filesize="134588" src="https://upload-images.jianshu.io/upload_images/1179389-44f9f35d1900a37d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>03、final 变量</h3>
<p>被 final 修饰的变量无法重新赋值。换句话说，final 变量一旦初始化，就无法更改。之前被一个小伙伴问过，什么是 effective final，什么是 final，这一点，我在之前的文章也有阐述过，所以这里再贴一下地址：</p>
<blockquote>
<p><a href="https://links.jianshu.com/go?to=http%3A%2F%2Fwww.itwanger.com%2Fjava%2F2020%2F02%2F14%2Fjava-final-effectively.html" target="_blank">http://www.itwanger.com/java/2020/02/14/java-final-effectively.html</a></p>
</blockquote>
<p>1）final 修饰的基本数据类型</p>
<p>来声明一个 final 修饰的 int 类型的变量：</p>
<pre><code class="java">final int age = 18;
</code></pre>
<p>尝试将它修改为 30，结果编译器生气了：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="444" data-height="173"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-9a9ffa2b51da5326.png" data-original-width="444" data-original-height="173" data-original-format="image/png" data-original-filesize="11617" src="https://upload-images.jianshu.io/upload_images/1179389-9a9ffa2b51da5326.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>2）final 修饰的引用类型</p>
<p>现在有一个普通的类 Pig，它有一个字段 name：</p>
<pre><code class="java">public class Pig &#123;
   private String name;

    public String getName() &#123;
        return name;
    &#125;

    public void setName(String name) &#123;
        this.name = name;
    &#125;
&#125;
</code></pre>
<p>在测试类中声明一个 final 修饰的 Pig 对象：</p>
<pre><code class="java"> final Pig pig = new Pig();
</code></pre>
<p>如果尝试将 pig 重新赋值的话，编译器同样会生气：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="441" data-height="163"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-d0ea690a7aba742c.png" data-original-width="441" data-original-height="163" data-original-format="image/png" data-original-filesize="14431" src="https://upload-images.jianshu.io/upload_images/1179389-d0ea690a7aba742c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>但我们仍然可以去修改 Pig 的字段值：</p>
<pre><code class="java">final Pig pig = new Pig();
pig.setName("特立独行");
System.out.println(pig.getName()); // 特立独行
</code></pre>
<p>3）final 修饰的字段</p>
<p>final 修饰的字段可以分为两种，一种是 static 的，另外一种是没有 static 的，就像下面这样：</p>
<pre><code class="java">public class Pig &#123;
   private final int age = 1;
   public static final double PRICE = 36.5;
&#125;
</code></pre>
<p>非 static 的 final 字段必须有一个默认值，否则编译器将会提醒没有初始化：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="260" data-height="61"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-54b8c26db4f00d49.png" data-original-width="260" data-original-height="61" data-original-format="image/png" data-original-filesize="4696" src="https://upload-images.jianshu.io/upload_images/1179389-54b8c26db4f00d49.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>static 的 final 字段也叫常量，它的名字应该为大写，可以在声明的时候初始化，也可以通过 static <a href="https://www.jianshu.com/p/30ef6bba51a9" target="_blank">代码块初始化</a>。</p>
<ol start="4">
<li>final 修饰的参数</li>
</ol>
<p>final 关键字还可以修饰参数，它意味着参数在方法体内不能被再修改：</p>
<pre><code class="java">public class ArgFinalTest &#123;
    public void arg(final int age) &#123;
    &#125;

    public void arg1(final String name) &#123;
    &#125;
&#125;
</code></pre>
<p>如果尝试去修改它的话，编译器会提示以下错误：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="536" data-height="294"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-d7cca15c6e1b7e51.png" data-original-width="536" data-original-height="294" data-original-format="image/png" data-original-filesize="26309" src="https://upload-images.jianshu.io/upload_images/1179389-d7cca15c6e1b7e51.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>04、总结</h3>
<p>亲爱的读者朋友，我应该说得很全面了吧？我想小王看到了这篇文章后一定会感谢我的良苦用心的，他毕竟是个积极好学的好同事啊。</p>
<p>如果觉得文章对你有点帮助，请微信搜索「 <strong>沉默王二</strong> 」第一时间阅读，回复「<strong>并发</strong>」更有一份阿里大牛重写的 Java 并发编程实战，从此再也不用担心面试官在这方面的刁难了。</p>
<blockquote>
<p>本文已收录 GitHub，<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fqinggee%2Fitwanger.github.io" target="_blank"><strong>传送门~</strong></a> ，里面更有大厂面试完整考点，欢迎 Star。</p>
</blockquote>
<p>我是沉默王二，一枚有颜值却靠才华苟且的程序员。<strong>关注即可提升学习效率，别忘了三连啊，点赞、收藏、留言，我不挑，嘻嘻</strong>。</p>
  
</div>
            