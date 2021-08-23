
---
title: 'unity愤怒的小鸟初级版的实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d76522db5b024867a3ac1a3abc83de07~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 18:21:09 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d76522db5b024867a3ac1a3abc83de07~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第23天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>之前已经写过几篇用unity写的小游戏博客，感觉还不错，那么我就继续写下去。 今天写的愤怒的小鸟初级版本。</p>
<p>愤怒的小鸟曾经是风靡全球的游戏，在玩法上就是用小鸟通过弹簧来射击猪。其中猪是由各种东西保护的。游戏规则也相对来说比较简单。</p>
<p>老规矩，先上效果图</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d76522db5b024867a3ac1a3abc83de07~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>场景比较简单，背景图是一个蓝色，然后中间摆放了各种物品，其实物体是用手工在前期就已经摆好的，所以这里面就不多说什么。直接进入主题，看代码。</p>
<pre><code class="copyable"> public float forceNeeded = 1000;
 
    float collisionForce(Collision2D coll) &#123;
        // Estimate a collision's force (speed * mass)
        float speed = coll.relativeVelocity.sqrMagnitude;
        if (coll.collider.GetComponent<Rigidbody2D>())
            return speed * coll.collider.GetComponent<Rigidbody2D>().mass;
        return speed;
    &#125;

    void OnCollisionEnter2D(Collision2D coll) &#123;
        if (collisionForce(coll) >= forceNeeded)
            Destroy(gameObject);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这部分代码是挂在猪的身上的，其实就是碰撞力大于预定的数值，这样才能让猪消灭。Destroy(gameObject)就是把猪消灭。猪没有额外的其他逻辑代码。</p>
<pre><code class="copyable"> public GameObject effect;

    void OnCollisionEnter2D(Collision2D coll) &#123;
        // Spawn Effect, then remove Script
        Instantiate(effect, transform.position, Quaternion.identity);
        Destroy(this);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个是碰撞到之后就自己被消灭，然后再释放特效，这个是冰的脚本。也是没有太多的逻辑在。</p>
<pre><code class="copyable">
 void OnMouseUp() &#123;
        // Disable isKinematic
        GetComponent<Rigidbody2D>().isKinematic = false;
        
        // Add the Force
        Vector2 dir = startPos - (Vector2)transform.position;
        GetComponent<Rigidbody2D>().AddForce(dir * force);

        // Remove the Script (not the gameObject)
        Destroy(this);
    &#125;

    void OnMouseDrag() &#123;        
        // Convert mouse position to world position
        Vector2 p = Camera.main.ScreenToWorldPoint(Input.mousePosition);

        // Keep it in a certain radius
        float radius = 1.8f;
        Vector2 dir = p - startPos;
        if (dir.sqrMagnitude > radius)
            dir = dir.normalized * radius;

        // Set the Position
        transform.position = startPos + dir;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>整份代码，应该最重要这一部分，这是写了弹叉的功能。包括了鼠标点击之下进行拖拽，然后再鼠标按键松开的效果。拖拽的功能用记录鼠标位置，拖动小鸟的位置。然后鼠标松开函数实现了计算发射方向和给小鸟增加一个力的过程。</p>
<p>这个是一个比较基础简单的游戏实例，有兴趣学unity的话，<strong>可以关注公众号：诗一样的代码</strong>，留言给我，我教你系统地学。</p></div>  
</div>
            