
---
title: '以全新的 Notion API，尝试全新的记账方式'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2021/05/16/253796374fb7d31938a6247d48224948.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Sun, 16 May 2021 07:05:13 GMT
thumbnail: 'https://cdn.sspai.com/2021/05/16/253796374fb7d31938a6247d48224948.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-e1f0100a><div class="content wangEditor-txt minHeight" data-v-e1f0100a><h3><strong>Matrix 首页推荐</strong></h3><p><a href="https://sspai.com/matrix" target="_blank">Matrix</a> 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。</p><p>文章代表作者个人观点，少数派仅对标题和排版略作修改。</p><hr><blockquote><p>The wait is over, Notion API is in public beta!</p></blockquote><p>——在 Notion 发来的邮件中如是写道。</p><p>是的，终于，Notion API 开放了公测，现在所有用户都可以去 Notion 创建自己的应用，并充分利用 Notion 提供的 API 来构筑完全属于自己的工作流。</p><p>也是为了体验 Notion API 带来的快乐，我尝试用它制作了一个记账小工具，可以方便导入支付宝、微信的账单，并对这些账目进行管理和核对。</p><h2>在 Notion 中设计数据表</h2><p>在当前 Notion API 的设计中，数据表的创建是在 Notion 网页端或者客户端完成，并不能直接通过 API 来实现。</p><p>在我的记账表格中，相关的数据表字段如下：</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/05/16/253796374fb7d31938a6247d48224948.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/05/16/253796374fb7d31938a6247d48224948.png" referrerpolicy="no-referrer"></figure><p>价格是一个 Number 字段，格式选择了 Yuan；标签是一个 Multi-select 字段，按自己的分类需求，对账目进行简单、快速而准确的标记；时间是 Date 字段，并选择了更符合中国人习惯的显示格式；来源是一个文本；创建于、更新于分别对应 Created time 和 Last edited time，由表格自动生成；星期是一个 Formula 字段，内容如下：</p><pre class="language-javascript"><code>replace(replace(replace(replace(replace(replace(replace(formatDate(prop("时间"), "d"), "6", "星期六"), "5", "星期五"), "4", "星期四"), "3", "星期三"), "2", "星期二"), "1", "星期一"), "0", "星期日") + ((formatDate(prop("时间"), "HHmm") == "0000") ? "" : (" | " + ((hour(prop("时间")) <= 7) ? "凌晨" : ((hour(prop("时间")) <= 10) ? "早上" : ((hour(prop("时间")) <= 15) ? "中午" : ((hour(prop("时间")) <= 21) ? "晚上" : "夜里"))))))</code></pre><p>这个公式可以根据前面的「时间」字段，从日期中取得星期，再从时间中取得时间段，便于快速查看。例如，2021/05/13 会提取成为「星期四」，而 8:52 则提取为「早上」。</p><p>账单条目的内容则填在页面标题中。</p><h2>创建 Notion 机器人</h2><p>我们在使用 Notion API 时，并不是以「账户」身份登录，来操作所有的数据表；而是通过创建一个个的机器人（称为 integration），每个机器人分别来完成不同的事务，并根据每个机器人所需涉及的数据表，分别对每个机器人进行访问授权。</p><p>在机器人 <a href="https://www.notion.so/my-integrations" target="_blank">管理页面</a> 中，只需要填入机器人名字，就可以快速创建一个机器人。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/05/16/7c75c9c3265488c18820a59a4ea6e413.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/05/16/7c75c9c3265488c18820a59a4ea6e413.png" referrerpolicy="no-referrer"></figure><p>提交（Submit）后，系统会给出一个复杂的密钥，点击 Show 记录。这个密钥可以随时在前述机器人管理页面中查看。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/05/16/db7e510fdb55402e0e12ede832ef356b.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/05/16/db7e510fdb55402e0e12ede832ef356b.png" referrerpolicy="no-referrer"></figure><p>创建完成后，回到之前的数据表中，点击 Share 并选择 Invite，把我们前面创建的机器人邀请进我们的数据表中。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/05/16/596564aa8f8af83f06604033ec542bd9.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/05/16/596564aa8f8af83f06604033ec542bd9.png" referrerpolicy="no-referrer"></figure><p>这样，我们的机器人就可以访问并编辑这个数据表了。</p><h2>Notion API 概述</h2><p>在 Notion <a href="https://developers.notion.com/">开发者网站</a> 中列举了 Notion 当前支持的所有 API 接口。Notion API 遵循 RESTful 设计风格，目前可以操作的资源及其对应的操作类型包括：</p><ul><li>数据表 Database<ul><li>获取指定数据表的字段等信息</li><li>过滤、排序后输出指定数据表的内容</li><li>查询所有允许操作的数据表</li></ul></li><li>页面 Page<ul><li>获取指定页面中各字段的值</li><li>创建新页面</li><li>更新指定页面中各字段的值</li></ul></li><li>块 Block<ul><li>列举指定页面中的所有块</li><li>在指定页面中创建新的块</li></ul></li><li>用户 User<ul><li>查看指定用户的信息</li><li>查看工作区中所有用户的信息（包括机器人）</li></ul></li><li>搜索 Search<ul><li>在有权限的范围内执行全局搜索</li></ul></li></ul><p>所有涉及数据的内容，无论是请求体还是响应体，都以 JSON 的形式呈现，十分优雅。</p><h2>借助 Python 访问 Notion API</h2><p>由于 Notion API 基于 HTTP 提供，因此可以使用 Python 的 <a href="https://docs.python-requests.org/en/master/" target="_blank">requests</a> 模块进行简单开发。</p><p>为了便于编写消息体，有一个小技巧是，可以先通过「<a href="https://developers.notion.com/reference/get-page" target="_blank">获取指定页面中各字段的值</a>」这一接口来拉取页面结构。</p><p>先在之前创建的数据表中手动填写一条内容，并复制该页面的网址中的 ID 部分，也就是下图中划线的部分。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/05/16/9811651cfeb67bbff0ffdf751ea3ed59.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/05/16/9811651cfeb67bbff0ffdf751ea3ed59.png" referrerpolicy="no-referrer"></figure><p>现在，就可以通过接口来获取这个页面的内容了。Python 代码如下：</p><pre class="language-python"><code>r = requests.request(
    "GET",
    "https://api.notion.com/v1/pages/4a2c9f40c27e478fba4de58af0787a69",
    headers=&#123;"Authorization": "Bearer " + token, "Notion-Version": "2021-05-13"&#125;,
)
print(r.text)</code></pre><p>得到的结果如下：</p><pre class="language-javascript"><code>&#123;
    "object": "page",
    "id": "4a2c9f40-c27e-478f-ba4d-e58af0787a69",
    "created_time": "2021-05-13T01:34:08.030Z",
    "last_edited_time": "2021-05-16T00:03:00.000Z",
    "parent": &#123;
        "type": "database_id",
        "database_id": "7b093d33-7d89-40c0-8985-86be964a3fc4"
    &#125;,
    "archived": false,
    "properties": &#123;
        "标签": &#123;
            "id": "+z@-",
            "type": "multi_select",
            "multi_select": [
                &#123;
                    "id": "0bd6b895-bf66-4a6a-ae99-13b162b02715",
                    "name": "🚦交通",
                    "color": "default"
                &#125;
            ]
        &#125;,
        "时间": &#123;
            "id": ":Wx1",
            "type": "date",
            "date": &#123; "start": "2021-05-13T08:52:00.000+08:00", "end": null &#125;
        &#125;,
        "价格": &#123; "id": "==wp", "type": "number", "number": 7.8 &#125;,
        "来源": &#123;
            "id": "TeSe",
            "type": "rich_text",
            "rich_text": [
                &#123;
                    "type": "text",
                    "text": &#123; "content": "支付宝", "link": null &#125;,
                    "annotations": &#123;
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    &#125;,
                    "plain_text": "支付宝",
                    "href": null
                &#125;
            ]
        &#125;,
        "星期": &#123;
            "id": "dQj*",
            "type": "formula",
            "formula": &#123; "type": "string", "string": "星期四 | 早上" &#125;
        &#125;,
        "更新于": &#123;
            "id": "qeNP",
            "type": "last_edited_time",
            "last_edited_time": "2021-05-16T00:03:00.000Z"
        &#125;,
        "创建于": &#123;
            "id": "&#123;pT[",
            "type": "created_time",
            "created_time": "2021-05-13T01:34:08.030Z"
        &#125;,
        "内容": &#123;
            "id": "title",
            "type": "title",
            "title": [
                &#123;
                    "type": "text",
                    "text": &#123; "content": "滴滴快车", "link": null &#125;,
                    "annotations": &#123;
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    &#125;,
                    "plain_text": "滴滴快车",
                    "href": null
                &#125;
            ]
        &#125;
    &#125;
&#125;</code></pre><p>为了记录一条新的账单条目，可以调用「<a href="https://developers.notion.com/reference/post-page">创建新页面</a>」的接口。事实上，「创建新页面」的请求体，和前面这个「获取指定页面中各字段的值」接口的响应体几乎完全一致，因此稍作修改就可以直接调用「创建新页面」的接口了。</p><p>消息体的内容为：</p><pre class="language-python"><code>body = &#123;
    "parent": &#123;"type": "database_id", "database_id": "7b093d33-7d89-40c0-8985-86be964a3fc4"&#125;,
    "properties": &#123;
        "标签": &#123;"multi_select": &#123;"name": "🚦交通"&#125;&#125;,
        "时间": &#123;"date": &#123;"start": arrow.get(time).to("+08").isoformat()&#125;&#125;,
        "价格": &#123;"number": 7.8&#125;,
        "来源": &#123;"rich_text": [&#123;"text": &#123;"content": "支付宝"&#125;&#125;]&#125;,
        "内容": &#123;"title": [&#123;"type": "text", "text": &#123;"content": "滴滴快车"&#125;&#125;]&#125;,
    &#125;,
&#125;</code></pre><p>将这个请求体和前面接口的响应体对比发现，请求体中所有字段全部来源于响应体，并且可以将响应体中不需要填写的、繁复的细节去除，而只留下我们关心的内容。这些细节会由 Notion 后台自动补足。</p><p>对应的 Python 请求代码如下：</p><pre class="language-python"><code>requests.request(
    "POST",
    "https://api.notion.com/v1/pages",
    json=body,
    headers=&#123;"Authorization": "Bearer " + token, "Notion-Version": "2021-05-13"&#125;,
)</code></pre><p>请求完成后，就可以在网页端或客户端的 Notion 上看到已经新增了一条记录。</p><h2>从支付宝和微信导出账单</h2><p>与 Notion 交互的部分已经完成，最后就是获取账单了。因为我日常的消费基本都是从支付宝或者微信走，所以统计的时候只需要导入微信和支付宝的账单即可。如果有零星使用现金或信用卡的，可以手动在 Notion 中记录。</p><p>微信的账单导出方法为：</p><ol><li>打开微信 APP</li><li>点击「我」</li><li>点击「支付」</li><li>点击「钱包」</li><li>点击「账单」</li><li>点击「常见问题」</li><li>点击「下载账单」</li><li>点击「用于个人对账」</li><li>选择「账单时间」</li><li>输入「邮箱地址」</li><li>输入「支付密码」</li></ol><p>稍候，账单就会发送到你的邮箱中。解压后是一个类似这样的逗号分隔（csv）文件：</p><pre class="language-null"><code>微信支付账单明细,,,,,,,,
微信昵称：[...],,,,,,,,
起始时间：[2021-04-26 00:00:00] 终止时间：[2021-04-28 22:29:42],,,,,,,,
导出类型：[全部],,,,,,,,
导出时间：[2021-04-28 22:29:59],,,,,,,,
,,,,,,,,
共5笔记录,,,,,,,,
收入：0笔 0.00元,,,,,,,,
支出：5笔 15.00元,,,,,,,,
中性交易：0笔 0.00元,,,,,,,,
注：,,,,,,,,
1. 充值/提现/理财通购买/零钱通存取/信用卡还款等交易，将计入中性交易,,,,,,,,
2. 本明细仅展示当前账单中的交易，不包括已删除的记录,,,,,,,,
3. 本明细仅供个人对账使用,,,,,,,,
,,,,,,,,
----------------------微信支付账单明细列表--------------------,,,,,,,,
交易时间,交易类型,交易对方,商品,收/支,金额(元),支付方式,当前状态,交易单号,商户单号,备注
2021-04-28 08:28:47,商户消费,花小猪打车,"滴滴出行服务",支出,¥1.60,中信银行,支付成功,420000101320,Gx,"/"
2021-04-27 09:03:47,商户消费,花小猪打车,"滴滴出行服务",支出,¥4.80,中信银行,支付成功,420000101020,fx,"/"
2021-04-26 13:28:02,商户消费,花小猪打车,"滴滴出行服务",支出,¥3.50,中信银行,支付成功,420000100520,hx,"/"
2021-04-26 11:51:41,商户消费,花小猪打车,"滴滴出行服务",支出,¥3.50,中信银行,支付成功,420000100220,7x,"/"
2021-04-26 08:35:30,商户消费,花小猪打车,"滴滴出行服务",支出,¥1.60,中信银行,支付成功,420000100820,ux,"/"</code></pre><p>在文件的前面几行都是一些统计信息，我们并不需要，因此只保留后半部分账单明细的内容。为了从中取出我们需要填入 Notion 中的内容，相应的 Python 代码可以是：</p><pre class="language-python"><code>def wechat(filepath):
    with open(filepath, "r", encoding="utf-8-sig", newline="") as f:
        lines = f.readlines()
        striped_lines = []
        start = False
        for line in lines:
            if not start:
                if line.startswith("----------------------"):
                    start = True
                continue
            striped_lines.append(line.strip())

        csvreader = csv.DictReader(striped_lines)
        for row in csvreader:
            t = arrow.get(row["交易时间"]).replace(tzinfo="+08").datetime
            c = row["商品"] + "，" + row["交易类型"] + "，" + row["交易对方"]
            a = row["金额(元)"]
            d = row["收/支"]
            print(t, c, a, d)
            if d == "收入":
                a = "-" + a[1:]
            elif d == "支出":
                a = a[1:]
            else:
                print("[未被计入]")
                continue
            Notion.add_bill(t, c, a, "微信")</code></pre><p>在这里，t、c、a 分别代码时间、内容、金额，而 Notion.add_bill 则是在前面一节所编写的与 Notion API 交互的函数。</p><p>与此相似的，支付宝也可以导出指定时间范围内的账单明细：</p><ol><li>在桌面浏览器中访问支付宝的 <a href="https://consumeprod.alipay.com/record/standard.htm">账单页</a></li><li>使用手机支付宝 APP 扫码登录</li><li>选择账单时间区间</li><li>点击「下载查询结果」</li></ol><p>支付宝的账单下载、解压后也是一个逗号分隔文件。将其用 Python 解析后，可以使用同样的 Notion.add_bill 函数处理并同步到 Notion 中。处理过程如下：</p><pre class="language-python"><code>def alipay(filepath):
    with open(filepath, "r", encoding="gbk", newline="") as f:
        lines = f.readlines()
        striped_lines = []
        start = False
        for line in lines:
            if not start:
                if line.startswith("----------------------------"):
                    start = True
                continue
            if line.startswith("----------------------------"):
                break
            l = regex.sub(r"\s+,", ",", line)
            striped_lines.append(l)

        csvreader = csv.DictReader(striped_lines)
        for row in csvreader:
            t = arrow.get(row["交易创建时间"]).replace(tzinfo="+08").datetime
            c = row["商品名称"] + "，" + row["交易对方"]
            a = row["金额（元）"]
            d = row["资金状态"]
            print(t, c, a, d)
            if a == "0":
                print("[未被计入]")
                continue
            elif d == "已收入" or d == "解冻":
                a = "-" + a
            elif d == "已支出" or d == "冻结":
                pass
            else:
                print("[未被计入]")
                continue
            Notion.add_bill(t, c, a, "支付宝")</code></pre><h2>相关链接</h2><p>致敬 <a href="https://github.com/jamalex/notion-py">notion-py</a>，它在官方 Notion API 鸽了又鸽的时光里为我们带来了便利：</p><p>所有机器人有统一的管理页面和申请入口：<a href="https://www.notion.so/my-integrations" target="_blank">https://www.notion.so/my-integrations</a></p><p>Notion 的 API 文档优雅而简洁：<a href="https://developers.notion.com/reference/intro" target="_blank">https://developers.notion.com/reference/intro</a></p><p>Notion 官方提供了 Node.js 的 SDK，不过便利性提升有限，举个例子：</p><pre class="language-javascript"><code> await notion.pages.create(&#123;
    parent: &#123;
        // ...
    &#125;,
    properties: &#123;
        标签: &#123;
            multi_select: [
                &#123;
                    name: '🚦交通',
                &#125;,
            ],
        &#125;,
        时间: &#123;
            // ...
        &#125;,
        // ...
    &#125;,
&#125;);</code></pre><p>可见，body 部分依然需要自己组装，无非是把 request 的请求换成了一个 notion.pages.create 直接调用，如果感兴趣的也可以尝试这个 <a href="https://github.com/makenotion/notion-sdk-js">SDK</a>。</p><p>如果不想自己亲自开发，也可以使用已经集成了 Notion 的低代码方案，例如 <a href="https://zapier.com/apps/notion/integrations">Zapier</a></p><p>总体而言，Notion API 还是带来了足够的惊喜。我也用过 notion-py 这样的非官方第三方库，相比之下，官方 API 提升了接口的稳定性、可靠性、易用性，也提供了更丰富的功能和更方便的调用方式。</p><p>不过，官方 API 库目前依然是 Beta 版本，许多功能尚未实现，例如文章正文中的 Block 只能添加（Append）而不能修改、数据表的字段必须预先创建而无法动态调整、机器人对数据表的权限必须「读写」而不能设为「只读」。相信 Notion API 在经过几次迭代之后就会变得足够好用，也会令 Notion 的生产力更进一级。</p><p>此外，除了可以为自己的 Notion 构建私有机器人，Notion 还允许将机器人设为公开，使所有用户都可以使用你的机器人。随着开发者们的加入，这样社区化的运营方式，必会诞生许多基于 Notion 的有趣应用。</p><p>> 下载 <a href="https://sspai.com/page/client" target="_blank">少数派 2.0 客户端</a>、关注<a href="https://sspai.com/s/J71e" target="_blank">少数派公众号</a>，让你的工作更有效率 ⏱</p><p>> 实用、好用的 <a href="https://sspai.com/mall" target="_blank">正版软件</a>，少数派为你呈现🚀</p></div><!----></div><div style="border:1px solid transparent;" data-v-e1f0100a></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-e1f0100a><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>81</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>27</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-2948" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E4%BB%A5%E5%85%A8%E6%96%B0%E7%9A%84%20Notion%20API%EF%BC%8C%E5%B0%9D%E8%AF%95%E5%85%A8%E6%96%B0%E7%9A%84%E8%AE%B0%E8%B4%A6%E6%96%B9%E5%BC%8F%E3%80%91%E4%B8%BA%E4%BA%86%E4%BD%93%E9%AA%8C%20Notion%20API%20%E5%B8%A6%E6%9D%A5%E7%9A%84%E5%BF%AB%E4%B9%90%EF%BC%8C%E6%88%91%E5%B0%9D%E8%AF%95%E7%94%A8%E5%AE%83%E5%88%B6%E4%BD%9C%E4%BA%86%E4%B8%80%E4%B8%AA%E8%AE%B0%E8%B4%A6%E5%B0%8F%E5%B7%A5%E5%85%B7%EF%BC%8C%E8%AE%A9%E6%88%91%E5%8F%AF%E4%BB%A5%E6%96%B9%E4%BE%BF%E5%9C%B0%E5%AF%BC%E5%85%A5%E6%94%AF%E4%BB%98%E5%AE%9D%E3%80%81%E5%BE%AE%E4%BF%A1%E7%9A%84%E8%B4%A6%E5%8D%95%EF%BC%8C%E5%B9%B6%E5%AF%B9%E8%BF%99%E4%BA%9B%E8%B4%A6%E7%9B%AE%E8%BF%9B%E8%A1%8C%E7%AE%A1%E7%90%86%E5%92%8C%E6%A0%B8%E5%AF%B9%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2021%2F05%2F16%2F5b0f7ecaaaf0a4b5ed66bbc52af7a356.png%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="icon icon-article_weibo right-16"></i></a><span><div role="tooltip" id="el-popover-4332" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><i class="icon icon-article_weixin right-16"></i></span><a href="https://twitter.com/share?text=%E3%80%90%E4%BB%A5%E5%85%A8%E6%96%B0%E7%9A%84%20Notion%20API%EF%BC%8C%E5%B0%9D%E8%AF%95%E5%85%A8%E6%96%B0%E7%9A%84%E8%AE%B0%E8%B4%A6%E6%96%B9%E5%BC%8F%E3%80%91%E4%B8%BA%E4%BA%86%E4%BD%93%E9%AA%8C%20Notion%20API%20%E5%B8%A6%E6%9D%A5%E7%9A%84%E5%BF%AB%E4%B9%90%EF%BC%8C%E6%88%91%E5%B0%9D%E8%AF%95%E7%94%A8%E5%AE%83%E5%88%B6%E4%BD%9C%E4%BA%86%E4%B8%80%E4%B8%AA%E8%AE%B0%E8%B4%A6%E5%B0%8F%E5%B7%A5%E5%85%B7%EF%BC%8C%E8%AE%A9%E6%88%91%E5%8F%AF%E4%BB%A5%E6%96%B9%E4%BE%BF%E5%9C%B0%E5%AF%BC%E5%85%A5%E6%94%AF%E4%BB%98%E5%AE%9D%E3%80%81%E5%BE%AE%E4%BF%A1%E7%9A%84%E8%B4%A6%E5%8D%95%EF%BC%8C%E5%B9%B6%E5%AF%B9%E8%BF%99%E4%BA%9B%E8%B4%A6%E7%9B%AE%E8%BF%9B%E8%A1%8C%E7%AE%A1%E7%90%86%E5%92%8C%E6%A0%B8%E5%AF%B9%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="icon icon-article_twitter right-16"></i></a></div></div><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            