
---
title: '从Python到Swift有多远？借鉴思路，编写更Swifty的正则匹配工具类｜项目复盘'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=8099'
author: 掘金
comments: false
date: Wed, 17 Mar 2021 00:43:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=8099'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#212122&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:8px;padding-bottom:8px&#125;.markdown-body h1&#123;color:#a0a0a0;font-size:38px;margin-top:32px;padding-top:32px&#125;.markdown-body h2&#123;color:#fff;background-color:#212122;width:fit-content;border-bottom-right-radius:100px;margin-top:47px;margin-bottom:16px;padding:4px 48px 4px 8px;line-height:1.7;font-size:30px;transition:all .3s ease-out&#125;.markdown-body h2:hover&#123;border-bottom-right-radius:50px;transition:all .3s ease-out&#125;.markdown-body h3&#123;font-size:24px;padding-left:8px;margin-top:32px;border-bottom:2px solid #c6c4c4;line-height:1.7&#125;.markdown-body h4&#123;font-size:20px;padding-left:8px;margin-top:32px;border-bottom:1px solid #ddd&#125;.markdown-body h5&#123;font-size:16px;margin-top:24px&#125;.markdown-body h6&#123;margin-top:16px;line-height:1.1&#125;.markdown-body p&#123;font-size:16px;text-align:start;white-space:normal;text-size-adjust:auto;line-height:2;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%;margin:auto;padding-left:8px;padding-right:8px&#125;.markdown-body hr&#123;border:none;border-top:4px double #212122;margin-top:32px;margin-bottom:32px;text-align:center&#125;.markdown-body hr:after&#123;content:"♥";display:inline-block;position:relative;top:-15px;padding:0 10px;color:#212122;font-size:18px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;background-color:#f1f1f1;color:#ef7060;font-size:14px;padding:.065em 6px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.7;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);margin:32px 16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-color:#212122;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);background-size:40px&#125;.markdown-body pre>code&#123;font-size:14px;padding:16px 8px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff;background:#272822&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:10px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;box-shadow:inset 0 0 6px rgba(0,0,0,.3);border-radius:3px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;border-radius:3px;box-shadow:inset 0 0 6px rgba(0,0,0,.3);background-color:#555&#125;.markdown-body a&#123;color:#ef7060;padding:2px;text-decoration:none;border-bottom:.125em solid #ef7060;border-radius:2px;box-shadow:inset 0 -.025em 0 #ef7060;transition:box-shadow .27s cubic-bezier(.77,0,.175,1),color .27s cubic-bezier(.77,0,.175,1)&#125;.markdown-body a:focus,.markdown-body a:hover&#123;outline:none;box-shadow:inset 0 -1.5em 0 #ef7060;color:#fff&#125;.markdown-body a:before&#123;content:"⇲ ";vertical-align:top;margin-left:2px;font-family:dart!important;font-size:12px;color:inherit;opacity:.7&#125;.markdown-body table&#123;background:#fbfbfb;border-radius:4px;border-collapse:collapse;margin:auto;padding:5px;width:95%;box-shadow:0 5px 10px rgba(0,0,0,.1);animation:float 5s infinite&#125;.markdown-body table th&#123;color:#fff;background:#212122;border-bottom:1px solid #9ea7af;border-right:1px solid #343a45;font-size:18px;padding:16px;text-align:left;vertical-align:middle&#125;.markdown-body table th:first-child&#123;border-top-left-radius:4px&#125;.markdown-body table th:last-child&#123;border-top-right-radius:4px;border-right:none&#125;.markdown-body table tr&#123;border-top:1px solid #c1c3d1;border-bottom:1px solid #c1c3d1;color:#666b85&#125;.markdown-body table tr:hover td&#123;background:#212122;color:#fff;border-top:1px solid #22262e&#125;.markdown-body table tr:first-child&#123;border-top:none&#125;.markdown-body table tr:last-child&#123;border-bottom:none&#125;.markdown-body table tr:nth-child(odd) td&#123;background:#f1f1f1&#125;.markdown-body table tr:nth-child(odd):hover td&#123;background:#212122&#125;.markdown-body table tr:last-child td:first-child&#123;border-bottom-left-radius:4px&#125;.markdown-body table tr:last-child td:last-child&#123;border-bottom-right-radius:4px&#125;.markdown-body table td&#123;background:#fbfbfb;padding:16px;text-align:left;vertical-align:middle;font-size:16px;border-right:1px solid #c1c3d1&#125;.markdown-body table td:last-child&#123;border-right:0&#125;.markdown-body blockquote&#123;color:#777;padding:1px 16px;margin:24px 0;border-left:4px solid #c6c4c4;background-color:#f1f1f1;transition:all .3s ease-out;border-radius:4px&#125;.markdown-body blockquote:hover&#123;border-left-color:#212122;background-color:#212122;color:#fff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:24px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:6px;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body span.math&#123;margin-left:32px;font-size:18px;font-weight:700&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:30.4px&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:19.2px&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:12.8px&#125;&#125;</style><h2 data-id="heading-0">项目简介</h2>
<p>一个字符串正则校验工具类，使用Swift中的enum实现并使用。</p>
<p>本文的思路亮点在于从Python使用的过程中，跳跃到Swift中的脑洞折腾方式，难点在于如何写出更Swifty的编码。</p>
<p>Python和Swift，API上的远方亲戚嘛。</p>
<h2 data-id="heading-1">项目背景</h2>
<p>做前端和App端一般都会涉及表单输入，校验手机号、邮箱等等一些输入字符串的校验，大多数时候，我们需要配合正则表达式加上系统层的API去做这些。</p>
<p>而我要做的，就是封装一个使用简单，一目了然的正则校验工具类。</p>
<h2 data-id="heading-2">实践过程</h2>
<h3 data-id="heading-3">从一个Python爬虫说起</h3>
<p>一切源于我在学习Python写爬虫，想要获取一些有用的信息。</p>
<p>嗯，你问我为啥明明写Swift的，怎么就变成从Python开始说起，因为我就是这么脑袋一抽风，编程脑洞这么顺手牵羊过来的。</p>
<p>嗯，你问我写爬虫爬什么东东？学Python就没干过什么正经事，你瞧隔壁这位：<a href="https://juejin.cn/post/6939875249013915655" target="_blank">偷偷告诉你中国小姐姐的真实Size！！</a>。</p>
<p>而使用Python写最简单的爬虫，是通过正则表达式来获取关键信息的。我们举个例子：</p>
<pre><code class="copyable"># 系统层级的判断正则表达式的类
import re
# 大名鼎鼎的网络请求库
import requests

def getPages() -> int:
    # ¸
    url = "有效网址"
    # 请求回来的响应
    response = requests.get(url)
    # 响应的html字符串
    html = response.text
    # 获取网页字符串中匹配的信息
    result = re.findall(r'>第 1 页，共 ([1-9]\d+) 页</span>', html)
    # 返回结果的第一次出现的值,也就是总页数
    return int(result[0])

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码里面除去网络请求，最有价值的代码下面这段:</p>
<pre><code class="copyable">result = re.findall(r'>第 1 页，共 ([1-9]\d+) 页</span>', html)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过re的findall函数，输入一个正则表达式与需要校验的字符串，去匹配结果集并以list的形式返回。</p>
<h3 data-id="heading-4">分析Python中的re中的源码</h3>
<p>来，我们先看看findall这个函数的源码，另外我觉得findall这个函数名一点也不Pythonic，你给我们整个find_all或者findAll都比这个好呀。</p>
<pre><code class="copyable">def findall(pattern, string, flags=0):
    """Return a list of all non-overlapping matches in the string.

    If one or more capturing groups are present in the pattern, return
    a list of groups; this will be a list of tuples if the pattern
    has more than one group.

    Empty matches are included in the result."""
    return _compile(pattern, flags).findall(string)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于Python编写函数的时候，是可以不带参数类型的，所以可能看起来有点懵圈，我简单分析一下：</p>
<hr>
<p>findall有三个参数：</p>
<p><strong>pattern是str类型</strong>，为正则表达式，你会好奇为啥我写的入参字符串是这样：<code>r'>第 1 页，共 ([1-9]\d+) 页</span>'</code>，这个<code>r‘’</code>表示的字符串原意表达式，我们都知道，html中有很多标签，会有\这样的字符串，如果不使用<code>r''</code>包裹起来，对于\这类字符串其实是需要转译的，<code>\\</code>才表示<code>\</code>
不了解的可以度娘一把：<a href="https://baike.baidu.com/item/%E8%BD%AC%E4%B9%89%E5%AD%97%E7%AC%A6/86397?fr=aladdin" target="_blank" rel="nofollow noopener noreferrer">转义字符</a></p>
<p><strong>string是str类型</strong>，为需要验证的字符串</p>
<p><strong>flags本质上一个枚举入参</strong>，默认给的0。</p>
<pre><code class="copyable">class RegexFlag(enum.IntFlag):
    ASCII = sre_compile.SRE_FLAG_ASCII # assume ascii "locale"
    IGNORECASE = sre_compile.SRE_FLAG_IGNORECASE # ignore case
    LOCALE = sre_compile.SRE_FLAG_LOCALE # assume current 8-bit locale
    UNICODE = sre_compile.SRE_FLAG_UNICODE # assume unicode "locale"
    MULTILINE = sre_compile.SRE_FLAG_MULTILINE # make anchors look for newline
    DOTALL = sre_compile.SRE_FLAG_DOTALL # make dot match newline
    VERBOSE = sre_compile.SRE_FLAG_VERBOSE # ignore whitespace and comments
    A = ASCII
    I = IGNORECASE
    L = LOCALE
    U = UNICODE
    M = MULTILINE
    S = DOTALL
    X = VERBOSE
    # sre extensions (experimental, don't rely on these)
    TEMPLATE = sre_compile.SRE_FLAG_TEMPLATE # disable backtracking
    T = TEMPLATE
    DEBUG = sre_compile.SRE_FLAG_DEBUG # dump pattern after compilation
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以用re.I作为最后一个入参，表示在正则查找中不在意大小写。</p>
<p><strong>_compile(pattern, flags).findall(string)</strong>，最后的这个方法已经涉及到其内部方法了，大致意思就说通过pattern与flag生成一个专门的正则匹配类，然后再去处理需要验证的字符串，通过注释，我们知道返回结果是一个list。</p>
<hr>
<h3 data-id="heading-5">分析Swift中的NSRegularExpression类</h3>
<p>你看我一上来，不务正业的巴拉巴拉说了一通Python，甚至连Python的源码都分析了一遍，为何？</p>
<p><strong>在我学习编程语言的时候，我经常会发出这样的感慨，这个函数真好用，哎，为啥Swift中就没有这个轮子呢？如果没有，可不可以自己尝试写呢？</strong></p>
<p>我最初的一个想法是Python中有re模块处理正则，那么Swift也会不会有类型的类呢？仔细一查，是有的————NSRegularExpression。</p>
<p>为了类比Python中的re，我贴一下NSRegularExpression的一些重要函数和参数枚举。</p>
<pre><code class="copyable">@available(iOS 4.0, *)
open class NSRegularExpression : NSObject, NSCopying, NSSecureCoding &#123;

    public init(pattern: String, options: NSRegularExpression.Options = []) throws
&#125;

extension NSRegularExpression &#123;    

    open func matches(in string: String, options: NSRegularExpression.MatchingOptions = [], range: NSRange) -> [NSTextCheckingResult]
    
&#125;

extension NSRegularExpression &#123;

    
    public struct Options : OptionSet &#123;

        public init(rawValue: UInt)

        
        public static var caseInsensitive: NSRegularExpression.Options &#123; get &#125;

        public static var allowCommentsAndWhitespace: NSRegularExpression.Options &#123; get &#125;

        public static var ignoreMetacharacters: NSRegularExpression.Options &#123; get &#125;

        public static var dotMatchesLineSeparators: NSRegularExpression.Options &#123; get &#125;

        public static var anchorsMatchLines: NSRegularExpression.Options &#123; get &#125;

        public static var useUnixLineSeparators: NSRegularExpression.Options &#123; get &#125;

        public static var useUnicodeWordBoundaries: NSRegularExpression.Options &#123; get &#125;
    &#125;
    
    public struct MatchingOptions : OptionSet &#123;

        public init(rawValue: UInt)

        public static var reportProgress: NSRegularExpression.MatchingOptions &#123; get &#125; 

        public static var reportCompletion: NSRegularExpression.MatchingOptions &#123; get &#125; 

        public static var anchored: NSRegularExpression.MatchingOptions &#123; get &#125; 

        public static var withTransparentBounds: NSRegularExpression.MatchingOptions &#123; get &#125; 

        public static var withoutAnchoringBounds: NSRegularExpression.MatchingOptions &#123; get &#125; 
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>init(pattern: String, options: NSRegularExpression.Options = [])</code>函数构造一个NSRegularExpression对象，传入的参数有两个<code>pattern: String</code>和<code>options: NSRegularExpression.Options = []</code>，分别是正则表达式和选项。</p>
<p>然后使用<code>matches(in string: String, options: NSRegularExpression.MatchingOptions = [], range: NSRange)</code>方法去获取匹配的结果。</p>
<h3 data-id="heading-6">从Python到Swift，实现同一个函数有多远？</h3>
<p>不远，也就换些API，从Pythonic到Swifty一点。</p>
<p>在iOS中，如果我们想要像Python一样爬一个网页，我们应该如何处理呢？</p>
<pre><code class="copyable">func getPages() -> Int? &#123;
    let urlString = "有效网址"
    
    /// 网址字符串转URL
    guard let url = URL(string: urlString) else &#123;
        return nil
    &#125;
    
    /// 获取网址的html
    guard let html = try? String(contentsOf: url, encoding: .utf8) else &#123;
        return nil
    &#125;
    
    /// Swift5特性,在##之间的字符串,可以不用\对特殊符号进行转义了
    let pattern = #">第 1 页，共 ([1-9]\d+) 页</span>"#
    
    /// 构造NSRegularExpression对象
    guard let regex = try? NSRegularExpression(pattern: pattern, options: []) else &#123;
        return nil
    &#125;
    
    /// 获取结果集
    let result = regex.matches(in: html, options: [], range: NSRange(location: 0, length: html.count))
    
    /// 获取第一个结果
    guard let firstResutl = result.first else &#123;
        return nil
    &#125;
    
    /// 通过一个结果的range去截取html上的有效字符串
    let num = (html as NSString).substring(with: firstResutl.range)
    
    /// 字符串转Int
    return Int(num)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>对比Python的爬虫写法，也许你会觉得Swift感觉很复杂，那是因为代码的严谨性，在创建URL的构造函数、NSRegularExpression的构造函数返回的都是可选类型，而且获取html字符串也是返回的可选类型，结果集result的第一个元素也有可能是为nil，所以使用了大量的guard去做守护操作。</p>
<p>基于上面的代码，你需要了解到：</p>
<ul>
<li>
<p>Swift内置的方法也是可以写爬虫的。<code>String(contentsOf: url, encoding: .utf8)</code></p>
</li>
<li>
<p>Swift中对于原意字符串也有支持的，字符串两端用<code>##</code>括起来即可。</p>
</li>
<li>
<p>Swift虽然写起来麻烦，不过考虑对于安全性和健壮性，是可以接受的。</p>
</li>
</ul>
<p>如果你对Swift的解包有疑惑，可以转移到我此前写的这篇文章：<a href="https://juejin.cn/post/6931154052776460302" target="_blank">Swift：解包的正确姿势</a></p>
<p>在Swift中，我们正则匹配字符串的核心代码在这里：</p>
<pre><code class="copyable">/// 构造NSRegularExpression对象
guard let regex = try? NSRegularExpression(pattern: pattern, options: []) else &#123;
    return nil
&#125;

/// 获取结果集
let result = regex.matches(in: html, options: [], range: NSRange(location: 0, length: html.count))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是和Python的re.findall函数内部实现函数<code>_compile(pattern, flags).findall(string)</code>非常类似呢?</p>
<p>到此，涉及Swift中通过正则表达式获取有效信息的类和方法就基本确定。下面就让我们进入正题，写一个Swifty的Regular工具类。</p>
<h3 data-id="heading-7">编写更Swifty的Regular工具类</h3>
<p>想到工具类，我们总是想着以Utils，虚基类，没有构造方法，静态方法等等，以下省略500字:</p>
<pre><code class="copyable">class RegularUtils &#123;
    /// 是否匹配电话号码
    ///
    /// - Parameters:
    ///   - pattern: 正则表达式字符串
    ///   - string: 待验证的字符串
    /// - Returns: Bool
    static func isContainPhoneNum(pattern:String, string: String) -> Bool &#123;&#125;
    .
    .
    .
    static func isContainEmail(pattern:String, string: String) -> Bool &#123;&#125;
    .
    .
    .
    private init() &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码当然没有问题，我们甚至可以继续扩展类方法，字符串中是否包含邮箱，包含车牌号等等。</p>
<p><strong>既然使用Swift编码，难道就不能写的更Swifty一点吗？</strong></p>
<hr>
<p><strong>就如文章一开始所说，我们可能需要校验的类型很多，手机号、邮箱、车牌号等等，每一个类型对于的正则也不同，有没有想过用Swift的枚举来构造这个工具类？</strong></p>
<p>使用枚举优势如下：</p>
<ol>
<li>
<p><strong>区分不同的校验类型</strong>，</p>
</li>
<li>
<p>通过<strong>Swift枚举带参</strong>的优势，直接将需要校验的字符串传入，</p>
</li>
<li>
<p>Swift的枚举<strong>本质上就是一个struct，所以可以添加方法、属性</strong>。</p>
</li>
</ol>
<hr>
<p>那么，就上一点enum写这个工具的思路吧：</p>
<p>首先突破对枚举只能表示状态的思维，带参数，带多个参数都是可以的。</p>
<p>枚举中有一个custom情况，相当于自定义正则类型，并与其待校验的字符串做匹配。</p>
<pre><code class="copyable">/// 正则表达式的判断
/// 这些枚举中的String都是待验证的字符串
/// - email: 邮箱
/// - phoneNum: 手机号
/// - carNum: 车牌号
/// - username: 用户名
/// - password: 密码
/// - nickname: 昵称
/// - checkCode: 验证码
/// - URL: url
/// - IP: ip地址
/// - idCard: 身份证
/// - custom: 自定义，注意custom枚举 其中有两个字符串, 第一个是待验证的字符串,第二个是正则表达式
public enum Regular &#123;
    case email(String)
    case phoneNum(String)
    case carNum(String)
    case username(String)
    case password(String)
    case nickname(String)
    case checkCode(String)
    case URL(String)
    case IP(String)
    case idCard(String)
    case custom(_ string: String, _ predicateString: String)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于一些固定正则式，我们可以在这个枚举中先声明：</p>
<pre><code class="copyable">extension Regular &#123;
    /// 样式
    private struct Pattern &#123;
        static let email = "^([a-z0-9_\\.-]+)@([\\da-z\\.-]+)\\.([a-z\\.]&#123;2,6&#125;)$"
        static let phoneNum = "^1[0-9]&#123;10&#125;$"
        static let carNum = "^[A-Za-z]&#123;1&#125;[A-Za-z_0-9]&#123;5&#125;$"
        static let username = "^[A-Za-z0-9_-]&#123;6,20&#125;+$"
        static let password = "^[a-zA-Z0-9]&#123;8,16&#125;+$"
        static let nickname = "^[\\u4e00-\\u9fa5]&#123;4,8&#125;$"
        static let url =  "^(https?:\\/\\/)?([\\da-z\\.-]+)\\.([a-z\\.]&#123;2,6&#125;)([\\/\\w \\.-]*)*\\/?$"
        static let ip = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.)&#123;3&#125;(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        static let checkCode = "^[0-9]&#123;4&#125;$"
        static let idCard = "^[1-9]\\d&#123;5&#125;[1-9]\\d&#123;3&#125;((0\\d)|(1[0-2]))(([0|1|2]\\d)|3[0-1])\\d&#123;3&#125;([0-9Xx])$"
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来，我们将涉及NSRegularExpression与返回NSTextCheckingResult结果的方法做简单的封装：</p>
<pre><code class="copyable">extension Regular &#123;

    /// 通过正则表达式获取一个NSRegularExpression
    ///
    /// - Parameter pattern: 正则表达式
    /// - Returns: NSRegularExpression
    private func regex(pattern: String, options: NSRegularExpression.Options = []) -> NSRegularExpression? &#123;
        return try? NSRegularExpression(pattern: pattern, options: options)
    &#125;
    
    /// 是否有匹配结果
    ///
    /// - Parameters:
    ///   - regex: NSRegularExpression
    ///   - string: 字符串
    /// - Returns: Bool
    private func isMatch(regex: NSRegularExpression?, string: String?) -> Bool &#123;
        guard let regex = regex, let string = string else &#123;
            return false
        &#125;
        
        return regex.matches(in: string, options: [], range: NSRange(location: 0, length: string.count)).count > 0
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，我们使用一个isMatch只读计算属性来完成这个正则表达类中的一个功能，<strong>用了返回字符串中是否有匹配内容：</strong></p>
<pre><code class="copyable">extension Regular &#123;
    public var isMatch: Bool &#123;
        let re: NSRegularExpression?
        let string: String
        switch self &#123;
        case let .email(str):
            re = regex(pattern: Pattern.email)
            string = str
        case let .phoneNum(str):
            re = regex(pattern: Pattern.phoneNum)
            string = str
        case let .carNum(str):
            re = regex(pattern: Pattern.carNum)
            string = str
        case let .username(str):
            re = regex(pattern: Pattern.username)
            string = str
        case let .password(str):
            re = regex(pattern: Pattern.password)
            string = str
        case let .nickname(str):
            re = regex(pattern: Pattern.nickname)
            string = str
        case let .URL(str):
            re = regex(pattern: Pattern.url)
            string = str
        case let .IP(str):
            re = regex(pattern: Pattern.ip)
            string = str
        case let .checkCode(str):
            re = regex(pattern: Pattern.checkCode)
            string = str
        case let .idCard(str):
            re = regex(pattern: Pattern.idCard)
            string = str
        case .custom(let str, let pattern):
            re = regex(pattern: pattern)
            string = str
        &#125;
        
        return isMatch(regex: re, string: string)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用的时候，我们这样写代码就可以啦：</p>
<pre><code class="copyable">let isEmail = Regular.email("season@qq.com").isMatch // true

let isContain = Regular.custom("html字符串", #">第 1 页，共 ([1-9]\d+) 页</span>"#).isMatch // false

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">思考总结</h2>
<ul>
<li>
<p>从Python到Swift，编程的思维即使是跨语言，很多时候也不会跨思路，在掌握一门编程语言的同时，有空去看看其他编程世界的精彩，在启发和拓展上往往会有意想不到的的收获。</p>
</li>
<li>
<p>代码想要写的更Swifty，并不是一朝一夕就从脑袋里崩出来的，从Utils工具类到enum工具类，是大量codeReview和学习的结果，多思考，多总结，才能将代码写的更Swifty。</p>
</li>
<li>
<p>合理的使用系统提供的轮子和方法，加以封装使用，会让编码愉快。有的时候，折腾很有必要。</p>
</li>
<li>
<p>Swift中枚举，比其他语言的枚举强大很多，善于使用枚举特性，带参特性，有的时候会有出人意料的效果。</p>
</li>
<li>
<p>Swift可以写爬虫的，虽然没有Python里的bs4，没有lxml，但是只有正则表达式使用的溜，也就是语言差异而已。</p>
</li>
<li>
<p>编程语言没有特定的墙，你所谓的墙都是自己给自己界定的。</p>
</li>
</ul>
<h3 data-id="heading-9">参考文章</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6931154052776460302" target="_blank">Swift：解包的正确姿势</a></p>
</blockquote>
<blockquote>
<p><a href="https://juejin.cn/post/6933045044978909192" target="_blank">Swift：Extension的使用小技巧 | 附Dart的Extension一点使用心得</a></p>
</blockquote>
<blockquote>
<p><a href="https://juejin.cn/post/6908628153241960455" target="_blank">Flutter：枚举的缺点</a></p>
</blockquote>
<p>本文正在参与「掘金 2021 春招闯关活动」, 点击查看<a href="https://juejin.cn/post/6933147477399109640" target="_blank">活动详情</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            