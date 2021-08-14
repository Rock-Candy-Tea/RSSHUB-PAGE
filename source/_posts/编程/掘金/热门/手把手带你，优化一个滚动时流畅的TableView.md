
---
title: '手把手带你，优化一个滚动时流畅的TableView'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/720bddcbfc8d4536be0f60aadd4f5120~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 17:52:56 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/720bddcbfc8d4536be0f60aadd4f5120~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<hr>
<p><strong>我的专栏</strong></p>
<ol>
<li><a href="https://juejin.cn/column/6970866662862127141" target="_blank" title="https://juejin.cn/column/6970866662862127141">iOS 底层原理探索</a></li>
<li><a href="https://juejin.cn/column/6987556760298979358" target="_blank" title="https://juejin.cn/column/6987556760298979358">iOS 底层原理探索 之 阶段总结</a></li>
</ol>
<hr>
<h2 data-id="heading-0">意识到我的问题</h2>
<p>平时使用手机的时间不算少，每天阅读新闻的时候会感觉到新闻类的app优化的还是很好的，TableView的Cell滚动的时候不会去加载显示图片内容，当一次滑动结束之后，Cell上的新闻图片便开始逐个的加载显示出来，所以整个滑动的过程是很流畅的。这中体验也是相当nice的。</p>
<h2 data-id="heading-1">我最开始的做法</h2>
<p>开发中TableView的使用是非常值频繁的，当TableViewCell上需要加载图片的时候，是一件比较头疼的事。因为，用户一边滑动TableView，TableView需要一边从网络获取图片。之前的操作都是放在 <code>cellForRowAtIndexPath</code> 中来处理，这就导致用户在滑动TableView的时候，会特别的卡（尤其是滑动特别快时），而且，手机的CPU使用率也会飙的非常的高。对于用户来说，这显然是一个十分糟糕的体验。</p>
<h3 data-id="heading-2">糟糕的图片显示 代码</h3>
<pre><code class="copyable">- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath &#123;
    
    ImageTableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"cell"];
    cell.index = indexPath;
    
    NSMutableDictionary *info = [self.dataSource objectAtIndex:cell.index.row];

    NSString *url = [info objectForKey: @"img" ];
    NSData *iData = [NSData dataWithContentsOfURL:[NSURL URLWithString: url ]];
    cell.img.image = [UIImage imageWithData:iData];
    cell.typeL.text = [NSString stringWithFormat:@"%ld-%ld", cell.index.section, cell.index.row];

    return cell;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">糟糕的手机CPU飙升率</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/720bddcbfc8d4536be0f60aadd4f5120~tplv-k3u1fbpfcp-watermark.image" alt="未命名.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">糟糕的用户滑动体验</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4aa942f2da0e4fa497ec4869117675a9~tplv-k3u1fbpfcp-watermark.image" alt="未命名1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不只是用户，对于开发这来讲，这也是不可以接受的体验。</p>
<p>平时接触并使用的app也非常的多，发现他们多处理方式就是，<code>当用户滑动列表的时候，不再加载图片，等用户的滑动结束之后，会开始逐一的加载图片。</code>这是非常好的优化思路，减轻了CPU的负担，也不会基本不会让用户感觉到页面滚动时候的卡顿。这也就是最开始我描述的我看新闻app的使用体验。</p>
<p>收到这个思路的启发，我们开始着手将上面糟糕的体验作一下优化吧。</p>
<h2 data-id="heading-5">总结思路开启优化之路</h2>
<p>那么，带着这个优化思路，我开始了对于这个TableView 的优化。</p>
<ul>
<li>首先，我们只加载当前用户可以看到的cell上的图片。</li>
<li>其次，我们一次只加载一张图片。</li>
</ul>
<p>要完成以上两点，图片的加载显示就不能在<code>cellForRowAtIndexPath</code>中完成，我们要定义并实现一个图片的加载显示方法，以便在合适的时机，调用刷新内容显示。</p>
<h3 data-id="heading-6">loadSeeImage 加载图片的优化</h3>
<pre><code class="copyable">#pragma mark load Images
- (void)loadSeeImage &#123;

    //记录本次加载的几张图片
    NSInteger loadC = 0;
    
    // 用户可以看见的cells
    NSArray *cells = [self.imageTableView visibleCells];
    
    // 调度组
    dispatch_group_t group = dispatch_group_create();
    
    for (int i = 0; i < cells.count; i++) &#123;
        
        ImageTableViewCell *cell = [cells objectAtIndex:i];
        
        NSMutableDictionary *info = [self.dataSource objectAtIndex:cell.index.row];
        NSString *url = [info objectForKey: @"img" ];
        
        NSString *data = [info objectForKey:@"data"];
        
        if ([data isKindOfClass:[NSData class]]) &#123;
            
            
        &#125;else &#123;
            
            // 添加调度则到我们的串行队列中去
            dispatch_group_async(group, self.loadQueue, ^&#123;
                
                NSData *iData = [NSData dataWithContentsOfURL:[NSURL URLWithString: url ]];
                NSLog(@" load image %ld-%ld ", cell.index.section, cell.index.row);
                if (iData) &#123;
                // 缓存
                    [info setValue:@"1" forKey:@"isload"];
                    [info setValue:iData forKey:@"data"];
                &#125;
                NSString *isload = [info objectForKey:@"isload"];
                
                if ([isload isEqualToString:@"0"]) &#123;
                    
                    dispatch_async(dispatch_get_main_queue(), ^&#123;

                        cell.img.image = [UIImage imageNamed:@""];
                    &#125;);                &#125;else &#123;
                    
                    if (iData) &#123;
                      
                        dispatch_async(dispatch_get_main_queue(), ^&#123;
                     //显示加载后的图片       
                            cell.img.image = [UIImage imageWithData:iData];
                        &#125;);
                    &#125;
                &#125;
                
            &#125;);
 
            if (i == cells.count - 1) &#123;

                dispatch_group_notify(group, dispatch_get_main_queue(), ^&#123;
                    // 全部加载完毕的通知
                    NSLog(@"load finished");
                &#125;);
            &#125;
            
            loadC += 1;
        &#125;
    &#125;
  
    NSLog(@"本次加载了 %ld 张图片", loadC);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其次就是 <code>loadSeeImage</code> 调用时机的处理，我们要做到用户在滑动列表之后加载，就是在下面两处加载：</p>
<pre><code class="copyable">- (void)scrollViewDidEndDecelerating:(UIScrollView *)scrollView   &#123;  
    
    [self loadSeeImage];
&#125;

- (void)scrollViewDidEndDragging:(UIScrollView *)scrollView willDecelerate:(BOOL)decelerate &#123;
    
    if (scrollView.isDragging || scrollView.isDecelerating || scrollView.isTracking) &#123;
        return;
    &#125;
    [self loadSeeImage];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，首次进入页面，列表数据加载完毕后，我们也要加载一次图片的哦。
好的下面看下优化后的结果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59959eb40f6a42be802867932095297b~tplv-k3u1fbpfcp-watermark.image" alt="优化xcode.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3163467ff509425e8fb4f81193e1f4fd~tplv-k3u1fbpfcp-watermark.image" alt="优化phone.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>CPU</code>占用率比之前最高的时候降低了一半多，app在滑动的时候也没有明显卡顿的地方。
完美。</p></div>  
</div>
            