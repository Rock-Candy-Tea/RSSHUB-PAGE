
---
title: '腾讯CDB复制选型及容量评估'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d85acd731dd64b858ef1ec51f82aa141~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 28 Apr 2021 02:02:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d85acd731dd64b858ef1ec51f82aa141~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">腾讯CDB复制选型及容量评估</h1>
<h2 data-id="heading-1"><strong>1. 压测目的：</strong></h2>
<ol>
<li>
<p>CDB复制模型选型</p>
</li>
<li>
<p>CDB容量规划参考</p>
</li>
</ol>
<p>CDB现在支持类型复制类型比较多，我这里选择以下几种复制类型压测对比： MySQL 5.6[异步|半同步|增强半同步]复制，5.7异步复制（当时5.7只支持异步复制).</p>
<p>CDB类型： 高可用版  4000MB内存， 200G存储空间</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d85acd731dd64b858ef1ec51f82aa141~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2"><strong>2. 压力机： 4G，2Core机器</strong></h2>
<p><strong>压测命令：</strong></p>
<p>sysbench /usr/local/share/sysbench/oltp_read_only.lua \</p>
<p>--db-driver=mysql \</p>
<p>--mysql-host=$&#123;DBIP&#125; \</p>
<p>--mysql-port=$&#123;DBPORT&#125; \</p>
<p>--mysql-db=wubx \</p>
<p>--mysql-user=wubx \</p>
<p>--mysql-password=‘XXXX' \</p>
<p>--tables=10 \</p>
<p>--table_size=5000000 \</p>
<p>--threads=200 \</p>
<p>--time=900 \</p>
<p>--report-interval=1 --percentile=99 run</p>
<p>（10张表， 每个表500万数据，200个并发压测），每个模型跑三次，取平均值。</p>
<h2 data-id="heading-3"><strong>3. 压测结果（2018年7月份的数据）：</strong></h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce01655ecd054c71bee3e40b73eee40b~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从结果上直观看来，感觉这4个差别不大。 基本是接近。 但为了直观对对比一下谁更好，再来一个图对比一下QPS：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6a6325785a84079b745b933340f8c65~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从这里看觉的CDB的MySQL 5.6增强半同步复制比MySQL5.7的异步复制性能还好。也可以说CDB的MySQL5.6优化的相当不错。（压测过程备节点延迟比较大）</p>
<h2 data-id="heading-4"><strong>4. 分析结果是不是值得值任</strong></h2>
<p>但再细想，这个结果也太接近了，基于这个原因来看了一下网卡流量：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2273171639a4dba89e1fdc6046a7b3d~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>发现网卡流量稳定在：165.XMB ，我用的压测机的网卡也只有1.5G, 感觉这个网卡流量非常吓人。咨询CDB的技术人员，原来他们CDB没有限制网卡流，单个CDB是万兆网卡（使用CDB的就笑吧），另外说明一个惊天秘密：CDB压测那会还没限制IO，这是大福利（这个资料有半年多时间了，现在是不是这样，不保证了，需要你有兴趣可以压测一下，自我验证一下）。 所以使用CDB还觉的响应时间慢的，请自查业务SQL，Schema设计优化吧。</p>
<p>基于这个测试，基本让我消除了CDB性能问题，对于容量规划只用考虑磁盘大小就行。所以不在继续压测。</p>
<h2 data-id="heading-5"><strong>5. 总结：</strong></h2>
<p>1. 对于复制选型：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9badfd43d9534000857fc11e615f135a~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于使用CDB环境，基本不用考虑运维这块，所以我建议可以直接上增强半同步就行，当然，如果为了使用5.7这个版本，只能去选择异步复制。</p>
<p>2. 容量规划</p>
<p>先考虑空间就行， 网卡流量，IO先不用考虑。 觉的有时想想腾讯做游戏基因在这里也是性能为王的一惯作风。</p>
<h2 data-id="heading-6"><strong>6. 思考：</strong></h2>
<p>      为什么CDB中MySQL 5.6复制看着比MySQL5.7还利害呢？  （下次给大家解密一下CDB MySQL 5.6的架构）</p>
<p>关注公众号：MySQLBeginner</p></div>  
</div>
            