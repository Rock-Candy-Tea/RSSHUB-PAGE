
---
title: 'Why React Needs Keys, Why It Matters'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e4c59573e6d4735bda96cc350db2300~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 18:57:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e4c59573e6d4735bda96cc350db2300~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Everyone uses React library all know that whenever we use a map to render, we need to pass the key. Otherwise, React will "yell" at us like this.<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e4c59573e6d4735bda96cc350db2300~tplv-k3u1fbpfcp-watermark.image" alt="Screenshot 2021-07-16 at 10.34.55 PM.png" loading="lazy" referrerpolicy="no-referrer">Oh nooo 😱😱, we need to pass the key now and most of the time we will pass like this.</p>
<pre><code class="copyable">list.map((l, idx) => &#123;
    return (
        <div key=&#123;idx&#125;>
            <span>&#123;l&#125;</span>
        </div>
    )
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Problem solved ✅, no more warning 😎But...😢😢</p>
<blockquote>
<p>Life is not a dream</p>
</blockquote>
<p>Let jump into an example of why "<em>Like is not a dream</em>"</p>
<p>Our manager gives us a task to create a dynamic Form with multiple Input fields, the user is able to enter their information and allow us to add or delete Input.<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fbf9ecb43174e38871c23750e7e03a5~tplv-k3u1fbpfcp-watermark.image" alt="ezgif.com-gif-maker.gif" loading="lazy" referrerpolicy="no-referrer">So</p>
<ul>
<li>We already know how to render the map in React library ✅</li>
<li>We already know how to use useState in React Hook with an array ✅</li>
<li>We also know method push/splice on array ✅</li>
</ul>
<p>Easy one lah 😎...Without the beat, we set up our application</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">const</span> [list, setList] = useState([]);

<span class="hljs-keyword">const</span> handleDelete = <span class="hljs-function">(<span class="hljs-params">idx</span>) =></span> &#123;
    list.splice(idx, <span class="hljs-number">1</span>);
    setList([...list]);
&#125;;

<span class="hljs-keyword">const</span> handleAdd = <span class="hljs-function">() =></span> &#123;
    list.push(<span class="hljs-string">`Information <span class="hljs-subst">$&#123;list.length + <span class="hljs-number">1</span>&#125;</span>`</span>);
    setList([...list]);
&#125;;

<span class="hljs-keyword">const</span> handleChange = <span class="hljs-function">(<span class="hljs-params">idx, l</span>) =></span> &#123;
    list[idx] = l;
    setList([...list]);
&#125;;

<span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
        &#123;list.map((l, idx) => &#123;
            return (
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;idx&#125;</span>></span>
                    &#123;FancyComponent(l, handleChange, idx)&#125;
                    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> handleDelete(idx)&#125;>Delete<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            );
        &#125;)&#125;
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> handleAdd()&#125;>Add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
&#125;

<span class="hljs-keyword">const</span> FancyComponent = <span class="hljs-function">(<span class="hljs-params">l, handleChange, idx</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> onChange = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
        e.preventDefault();
        handleChange(idx, e.currentTarget.value);
    &#125;;
   
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">defaultValue</span>=<span class="hljs-string">&#123;l&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(e)</span> =></span> onChange(e)&#125; /></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Here is <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fnifty-lumiere-eepxh%3Ffile%3D%2Fsrc%2FApp.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/nifty-lumiere-eepxh?file=/src/App.js" ref="nofollow noopener noreferrer">Playground</a></p>
<p>Done!!! Feel super awesome 😁💪, it works like charm. We pass to our manager, our manager like 🤩😍</p>
<p>A few moment later, our manager comes back again. We thought he would asking for the beer to appreciate but he said he found a bug 😱😭. The deletion didn't work as expected 🥺<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31710dc816c146f99bda20a76218f83c~tplv-k3u1fbpfcp-watermark.image" alt="ezgif.com-gif-maker (1).gif" loading="lazy" referrerpolicy="no-referrer">After he modified Information 3 to Information 323, deleted this input but the application deleted Information 4, Information 5</p>
<p>We like whattt 😱😱😱, how it could be possible!!!, it just only 50 lines of codes...</p>
<p>After put the console.log everywhere, googling, StackOverflow... We found the problem is <strong>the index we passed before</strong> is changed it makes ReactJS confused and render incorrect.</p>
<p>And if we don't use idx anymore, use content instead. Problem solved! ✅</p>
<pre><code class="hljs language-js copyable" lang="js"><div className=<span class="hljs-string">"App"</span>>
    &#123;list.map(<span class="hljs-function">(<span class="hljs-params">l, idx</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;l&#125;</span>></span>
                &#123;FancyComponent(l, handleChange, idx)&#125;
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> handleDelete(idx)&#125;>Delete<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
         );
     &#125;)&#125;
    <button onClick=&#123;<span class="hljs-function">() =></span> handleAdd()&#125;>Add</button>
</div<
<span class="copy-code-btn">复制代码</span></code></pre>
<p>PS: Still has an issue, waiting for anyone to figure it out. 😉</p>
<p>So now you might wonder that it is React's bug?!. No, it is not React's bug. Let's deep dive into it</p>
<p>If you noticed that when we change the value of the input, it works perfectly but deleting didn't work well because "changing" and "moving" state it is very different. When "moving" React needs to know what key of component is which we passed as an index of the array and deleting is changing the index hence it makes ReactJS confused. So why React don't make the by itself.</p>
<p>Dan's explanation:</p>
<blockquote>
<p>React can’t make up a good key itself. Only <em>you</em> know how your data is structured and whether two circles in two renders are “the same” circle conceptually (even if all of its data changed) or not. Usually, you’d use an ID generated during data creation. Such as from a databaseReact can’t make up a good key itself. Only <em>you</em> know how your data is structured and whether two circles in two renders are “the same” circle conceptually (even if all of its data changed) or not. Usually, you’d use an ID generated during data creation. Such as from a database</p>
</blockquote>
<p>It is 100% true, as an example, we go through above that it is a business requirement, as library React doesn't know what the key should be which only us, developers created those components.</p>
<p><strong>What happens if you pass a random key every time?</strong></p>
<blockquote>
<p>Well, you’re telling React that circles are_never_the same between renders. So if you have some state inside of them, it will be lost after every re-render. React will destroy and recreate every circle because you told it to.</p>
</blockquote>
<p>We will lose the "beauty" of ReactJS, isn't it? I believe no one wants to re-render every single time unless you have special requirements.</p>
<p>You might wonder why this topic pops up now, the concept of Keys has been there for a long time. ReactJS core team has started to built-in deep support Animation so Keys will play a big role there and in the future.</p>
<p><strong>Bonus:</strong></p>
<ul>
<li>ReactJS Core will update documentation about keys for more details.</li>
<li>You might have awake of ReactJS 18 Alpha out and you also can follow ReactJS 18 working group to follow what the changes and new APIs are.</li>
<li>React 18: <a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2Fblog%2F2021%2F06%2F08%2Fthe-plan-for-react-18.html" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/blog/2021/06/08/the-plan-for-react-18.html" ref="nofollow noopener noreferrer">reactjs.org/blog/2021/0…</a></li>
<li>React 18 Working Group: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18" ref="nofollow noopener noreferrer">github.com/reactwg/rea…</a></li>
</ul>
<p>Hope you enjoy the article 😊</p></div>  
</div>
            