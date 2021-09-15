
---
title: '面试急转弯：List 如何一边遍历，一边删除？'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://picsum.photos/400/300?random=2100'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=2100'
---

<div>   
<blockquote>
<p>这是最近面试时被问到的1道面试题，本篇博客对此问题进行总结分享。</p>
</blockquote>
<h1>新手常犯的错误</h1>
<p>可能很多新手（包括当年的我，哈哈）第一时间想到的写法是下面这样的：</p>
<pre><code class="java">public static void main(String[] args) &#123;
    List<String> platformList = new ArrayList<>();
    platformList.add("博客园");
    platformList.add("CSDN");
    platformList.add("掘金");
    for (String platform : platformList) &#123;
        if (platform.equals("博客园")) &#123;
            platformList.remove(platform);
        &#125;
    &#125;
    System.out.println(platformList);
&#125;
</code></pre>
<p>然后满怀信心的去运行，结果竟然抛 <code>java.util.ConcurrentModificationException</code> 异常了，翻译成中文就是：并发修改异常。</p>
<p>是不是很懵，心想这是为什么呢？</p>
<p>让我们首先看下上面这段代码生成的字节码，如下所示：</p>
<p>由此可以看出，<code>foreach</code> 循环在实际执行时，其实使用的是 <code>Iterator</code> ，使用的核心方法是<code>hasnext()</code>和<code>next()</code>。</p>
<p>然后再来看下 <code>ArrayList</code> 类的 <code>Iterator</code> 是如何实现的呢？</p>
<p>可以看出，调用 <code>next()</code> 方法获取下一个元素时，第一行代码就是调用了<code>checkForComodification()</code>;，而该方法的核心逻辑就是比较 <code>modCount</code> 和 <code>expectedModCount</code> 这2个变量的值。</p>
<p>在上面的例子中，刚开始 <code>modCount</code> 和 <code>expectedModCount</code> 的值都为3，所以第1次获取元素"博客园"是没问题的，但是当执行完下面这行代码时：</p>
<pre><code class="java">platformList.remove(platform);
</code></pre>
<p><code>modCount</code> 的值就被修改成了4。</p>
<p>所以在第2次获取元素时，<code>modCount</code> 和 <code>expectedModCount</code> 的值就不相等了，所以抛出了 <code>java.util.ConcurrentModificationException</code> 异常。</p>
<p>既然不能使用 <code>foreach</code> 来实现，那么我们该如何实现呢？</p>
<p>主要有以下3种方法：</p>
<ul>
<li><p>使用 <code>Iterator</code> 的 <code>remove()</code> 方法</p></li>
<li><p>使用<code>for</code> 循环正序遍历</p></li>
<li><p>使用 <code>for</code> 循环倒序遍历</p></li>
</ul>
<p>接下来一一讲解。</p>
<h2>使用 <code>Iterator</code> 的 <code>remove()</code> 方法</h2>
<p>使用 <code>Iterator</code> 的 <code>remove()</code>方法的实现方式如下所示：</p>
<pre><code class="java">public static void main(String[] args) &#123;
    List<String> platformList = new ArrayList<>();
    platformList.add("博客园");
    platformList.add("CSDN");
    platformList.add("掘金");
    Iterator<String> iterator = platformList.iterator();
    while (iterator.hasNext()) &#123;
        String platform = iterator.next();
        if (platform.equals("博客园")) &#123;
            iterator.remove();
        &#125;
    &#125;
    System.out.println(platformList);
&#125;
</code></pre>
<p>输出结果为：</p>
<pre><code class="java">[CSDN, 掘金]
</code></pre>
<p>为什么使用 <code>iterator.remove();</code> 就可以呢？</p>
<p>让我们看下它的源码：</p>
<p>可以看出，每次删除一个元素，都会将 <code>modCount</code> 的值重新赋值给 <code>expectedModCount</code>，这样2个变量就相等了，不会触发 <code>java.util.ConcurrentModificationException</code> 异常。</p>
<h2>使用 <code>for</code> 循环正序遍历</h2>
<p>使用 <code>for</code> 循环正序遍历的实现方式如下所示：</p>
<pre><code class="java">public static void main(String[] args) &#123;
    List<String> platformList = new ArrayList<>();
    platformList.add("博客园");
    platformList.add("CSDN");
    platformList.add("掘金");
    for (int i = 0; i < platformList.size(); i++) &#123;
        String item = platformList.get(i);
        if (item.equals("博客园")) &#123;
            platformList.remove(i);
            i = i - 1;
        &#125;
    &#125;
    System.out.println(platformList);
&#125;
</code></pre>
<p>这种实现方式比较好理解，就是通过数组的下标来删除，不过有个注意事项就是删除元素后，要修正下下标的值：</p>
<pre><code class="java">i = i - 1;
</code></pre>
<p>为什么要修正下标的值呢？</p>
<p>因为刚开始元素的下标是这样的：</p>
<p>第1次循环将元素"博客园"删除后，元素的下标变成了下面这样：</p>
<p>第2次循环时i的值为1，也就是取到了元素”掘金“，这样就导致元素 <code>"CSDN"</code> 被跳过检查了，所以删除完元素后，我们要修正下下标，这也是上面代码中 <code>i = i - 1;</code> 的用途。更多面试问题可以关注微信订阅号码匠笔记回复面试获取</p>
<h2>使用 <code>for</code> 循环倒序遍历</h2>
<p>使用 <code>for</code> 循环倒序遍历的实现方式如下所示：</p>
<pre><code class="java">public static void main(String[] args) &#123;
    List<String> platformList = new ArrayList<>();
    platformList.add("博客园");
    platformList.add("CSDN");
    platformList.add("掘金");
    for (int i = platformList.size() - 1; i >= 0; i--) &#123;
        String item = platformList.get(i);
        if (item.equals("掘金")) &#123;
            platformList.remove(i);
        &#125;
    &#125;
    System.out.println(platformList);
&#125;
</code></pre>
<p>这种实现方式和使用 <code>for</code> 循环正序遍历类似，不过不用再修正下标，因为刚开始元素的下标是这样的：</p>
<p>第1次循环将元素"掘金"删除后，元素的下标变成了下面这样：</p>
<p>第2次循环时i的值为1，也就是取到了元素”CSDN“，不会导致跳过元素，所以不需要修正下标。</p>
  
</div>
            