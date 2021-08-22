
---
title: 'unity像素鸟实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f38b9f9a47410fac0ccb20f6717b77~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 18:24:46 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f38b9f9a47410fac0ccb20f6717b77~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第22天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>之前已经写过几篇用unity写的小游戏博客，感觉还不错，那么我就继续写下去。 今天写的是像素鸟。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f38b9f9a47410fac0ccb20f6717b77~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个像素鸟小游戏玩法也简单，就是点击屏幕，然后小鸟会往上飞一下，不然就会往下掉。然后过程中会有各种水管，我们需要穿越水管，然后得分。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/811ed04f07974624920411cb274a92b4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>先看场景对象有什么，这里面有bg01也就是背景，然后gameover也就是游戏失败时候会弹出来的背景框。ready就是准备动作。bird是鸟。roads是管道。score是显示分数。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28bc8a967c66426b9e8f629ea52d74b9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>再来看看对象都写了哪些？其实基本上每一个游戏主题都挂上了相应的游戏脚本。其中最重要的肯定是bird脚本，这是控制鸟主角的动作的。</p>
<pre><code class="copyable">
// Use this for initialization
void Start () &#123;
body = gameObject.GetComponent<Rigidbody2D>();
initPos = gameObject.transform.position;
&#125;

// Update is called once per frame
void Update () &#123;
if(Input.GetButtonDown("Fire1"))&#123;
body.AddForce(force);
&#125;
&#125;

public void reset() &#123;
body.isKinematic = true;
gameObject.transform.position = initPos;
gameObject.transform.eulerAngles = Vector3.zero;
GetComponent<Animator>().enabled = true;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>鸟的动作主要是有三个函数，一开始在start函数里面得到鸟的刚体和位置。在游戏逻辑update中当按下了“Fire1”键，也就是电脑的鼠标左键时候，鸟作为刚体就会往上增加一个力，这个力是为了让鸟有一个向上的跳动。注意，这里必须要让鸟是刚体，他才会受力的。</p>
<p>最后是reset()函数，也就是重新配置鸟的位置，欧拉角，动画等属性而已。</p>
<pre><code class="copyable">
public void gen() &#123;
zhuzi[0].SetActive(true);
zhuzi[1].SetActive(true);
Vector3 p = zhuzi[0].transform.localPosition;
float vv = Random.value;
p.y = Mathf.Lerp(down, upper, vv);
zhuzi[0].transform.localPosition = p;

p = zhuzi[1].transform.localPosition;
 vv = Random.value;
p.y = Mathf.Lerp(down, upper, vv);
zhuzi[1].transform.localPosition = p;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这段代码是写柱子的随机生成，其实就是随机生成柱子的位置。这里面只管了生成。</p>
<pre><code class="copyable">void Update () &#123;
 Vector3 pos = trans.position;
pos.x -= speed * Time.deltaTime;
trans.position = pos;
if(pos.x <= -1.6f - 3.35f*idx) &#123;
Vector3 pp = roads[idx%2].transform.position;
pp.x += 3.35f;
idx++;
roads[idx%2].transform.position = pp;
if(isBegin)&#123;
roads[idx%2].GetComponent<roadGen>().gen();
&#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后这一段代码写的是柱子的移动。其实看起来是鸟在动，其实鸟一直在中心的位置没有变化，而是柱子一直在向左移动。</p>
<p>这个是一个比较基础简单的游戏实例，有兴趣学unity的话，<strong>可以关注公众号：诗一样的代码</strong>，留言给我，我教你系统地学。</p></div>  
</div>
            