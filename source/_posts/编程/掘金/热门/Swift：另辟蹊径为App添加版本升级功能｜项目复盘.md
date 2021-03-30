
---
title: 'Swift：另辟蹊径为App添加版本升级功能｜项目复盘'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c5039f464a148e7a4efe8e721d04441~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 18 Mar 2021 00:58:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c5039f464a148e7a4efe8e721d04441~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#212122&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:8px;padding-bottom:8px&#125;.markdown-body h1&#123;color:#a0a0a0;font-size:38px;margin-top:32px;padding-top:32px&#125;.markdown-body h2&#123;color:#fff;background-color:#212122;width:fit-content;border-bottom-right-radius:100px;margin-top:47px;margin-bottom:16px;padding:4px 48px 4px 8px;line-height:1.7;font-size:30px;transition:all .3s ease-out&#125;.markdown-body h2:hover&#123;border-bottom-right-radius:50px;transition:all .3s ease-out&#125;.markdown-body h3&#123;font-size:24px;padding-left:8px;margin-top:32px;border-bottom:2px solid #c6c4c4;line-height:1.7&#125;.markdown-body h4&#123;font-size:20px;padding-left:8px;margin-top:32px;border-bottom:1px solid #ddd&#125;.markdown-body h5&#123;font-size:16px;margin-top:24px&#125;.markdown-body h6&#123;margin-top:16px;line-height:1.1&#125;.markdown-body p&#123;font-size:16px;text-align:start;white-space:normal;text-size-adjust:auto;line-height:2;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%;margin:auto;padding-left:8px;padding-right:8px&#125;.markdown-body hr&#123;border:none;border-top:4px double #212122;margin-top:32px;margin-bottom:32px;text-align:center&#125;.markdown-body hr:after&#123;content:"♥";display:inline-block;position:relative;top:-15px;padding:0 10px;color:#212122;font-size:18px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;background-color:#f1f1f1;color:#ef7060;font-size:14px;padding:.065em 6px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.7;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);margin:32px 16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-color:#212122;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);background-size:40px&#125;.markdown-body pre>code&#123;font-size:14px;padding:16px 8px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff;background:#272822&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:10px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;box-shadow:inset 0 0 6px rgba(0,0,0,.3);border-radius:3px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;border-radius:3px;box-shadow:inset 0 0 6px rgba(0,0,0,.3);background-color:#555&#125;.markdown-body a&#123;color:#ef7060;padding:2px;text-decoration:none;border-bottom:.125em solid #ef7060;border-radius:2px;box-shadow:inset 0 -.025em 0 #ef7060;transition:box-shadow .27s cubic-bezier(.77,0,.175,1),color .27s cubic-bezier(.77,0,.175,1)&#125;.markdown-body a:focus,.markdown-body a:hover&#123;outline:none;box-shadow:inset 0 -1.5em 0 #ef7060;color:#fff&#125;.markdown-body a:before&#123;content:"⇲ ";vertical-align:top;margin-left:2px;font-family:dart!important;font-size:12px;color:inherit;opacity:.7&#125;.markdown-body table&#123;background:#fbfbfb;border-radius:4px;border-collapse:collapse;margin:auto;padding:5px;width:95%;box-shadow:0 5px 10px rgba(0,0,0,.1);animation:float 5s infinite&#125;.markdown-body table th&#123;color:#fff;background:#212122;border-bottom:1px solid #9ea7af;border-right:1px solid #343a45;font-size:18px;padding:16px;text-align:left;vertical-align:middle&#125;.markdown-body table th:first-child&#123;border-top-left-radius:4px&#125;.markdown-body table th:last-child&#123;border-top-right-radius:4px;border-right:none&#125;.markdown-body table tr&#123;border-top:1px solid #c1c3d1;border-bottom:1px solid #c1c3d1;color:#666b85&#125;.markdown-body table tr:hover td&#123;background:#212122;color:#fff;border-top:1px solid #22262e&#125;.markdown-body table tr:first-child&#123;border-top:none&#125;.markdown-body table tr:last-child&#123;border-bottom:none&#125;.markdown-body table tr:nth-child(odd) td&#123;background:#f1f1f1&#125;.markdown-body table tr:nth-child(odd):hover td&#123;background:#212122&#125;.markdown-body table tr:last-child td:first-child&#123;border-bottom-left-radius:4px&#125;.markdown-body table tr:last-child td:last-child&#123;border-bottom-right-radius:4px&#125;.markdown-body table td&#123;background:#fbfbfb;padding:16px;text-align:left;vertical-align:middle;font-size:16px;border-right:1px solid #c1c3d1&#125;.markdown-body table td:last-child&#123;border-right:0&#125;.markdown-body blockquote&#123;color:#777;padding:1px 16px;margin:24px 0;border-left:4px solid #c6c4c4;background-color:#f1f1f1;transition:all .3s ease-out;border-radius:4px&#125;.markdown-body blockquote:hover&#123;border-left-color:#212122;background-color:#212122;color:#fff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:24px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:6px;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body span.math&#123;margin-left:32px;font-size:18px;font-weight:700&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:30.4px&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:19.2px&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:12.8px&#125;&#125;</style><h2 data-id="heading-0">项目简介</h2>
<p>这篇文章，其实和之前那篇有那么一点点联系，我们考虑用Swift原生进行爬虫。</p>
<blockquote>
<p><a href="https://juejin.cn/post/6940540693127528462" target="_blank">从Python到Swift有多远？借鉴思路，编写更Swifty的正则匹配工具类｜项目复盘</a></p>
</blockquote>
<p>本文的亮点在于：用Swift爬AppStore的数据，进而解析数据，分析App版本，从而完成版本升级功能。</p>
<p>本文难点是真的可以这样操作么？这样可以吗？尝试，尝试了才知道结果。编码上基本上没有太多，也不复杂的，而关键在于思路是怎么来的，为什么这么做。</p>
<h2 data-id="heading-1">项目背景</h2>
<p>为App添加版本升级的功能，基本上在现在开发中很常见，偶尔也会在面试中提及。稍微有点开发经验的大佬们，大致思路如下：</p>
<blockquote>
<p>App的后台管理有一个版本配置信息，里面保存了一些信息：版本号，是否强制升级，是否正在审核等。App端在某个时机出调用某一个接口，网络请求，获取版本配置信息，进而在App端弹窗提示，进行强制升级；同时注意在App正在进行审核是规避类似升级提示的弹窗。</p>
</blockquote>
<p>流程图如下：</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c5039f464a148e7a4efe8e721d04441~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>非常简单，对吧？那么来一个假设：</p>
<p><strong>如果，注意是如果。</strong></p>
<p><strong>如果App端服务器没有这么一个后台版本信息配置功能，没有接口可以获取App的版本配置信息，如何为App添加版本升级功能？</strong></p>
<p><strong>也就是说App从App后台获取数据这条路断了，用什么数据去判断版本号，进行版本升级控制?</strong></p>
<h2 data-id="heading-2">实践过程</h2>
<h3 data-id="heading-3">先爬个虫压压惊：</h3>
<p>某一次Python的爬虫行为，让我找到了突破口，是的，没错，又是从Python开始的：</p>
<pre><code class="copyable">import requests

def getWeiXinAppStoreInfo():
    url = "http://itunes.apple.com/cn/lookup?id=414478124"
    # 请求回来的响应
    response = requests.get(url)
    # 响应的网页字符串
    text = response.text
    print(text)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看看text拿到的是什么数据，下面是格式化后的：</p>
<pre><code class="copyable">&#123;
    "resultCount":1,
    "results":[
        &#123;
            "screenshotUrls":[
                "https://is4-ssl.mzstatic.com/image/thumb/Purple114/v4/58/b2/69/58b2695c-e340-bf3d-ec8d-b317ae89aea3/pr_source.png/392x696bb.png",
                "https://is1-ssl.mzstatic.com/image/thumb/Purple114/v4/7f/34/e8/7f34e8b8-1e5b-854b-556c-5fdfa07fa947/pr_source.png/392x696bb.png",
                "https://is5-ssl.mzstatic.com/image/thumb/Purple124/v4/a0/aa/18/a0aa18e8-e94c-3333-0689-00841259c733/pr_source.png/392x696bb.png",
                "https://is1-ssl.mzstatic.com/image/thumb/Purple114/v4/83/af/72/83af72ff-a73d-9ad3-5679-234a170c08e1/pr_source.png/392x696bb.png",
                "https://is2-ssl.mzstatic.com/image/thumb/PurpleSource124/v4/c3/be/79/c3be7974-1083-1c01-c12f-bf7acd88321c/0356f5e8-253a-46b0-aae1-34eef8f19d38_1.1.jpg/392x696bb.jpg",
                "https://is4-ssl.mzstatic.com/image/thumb/PurpleSource124/v4/8e/93/fe/8e93fedd-a991-3fc0-2792-17900195ec10/8fb78965-9a18-4c54-b98d-54a277be936e_2.1.jpg/392x696bb.jpg"
            ],
            "ipadScreenshotUrls":[
                "https://is1-ssl.mzstatic.com/image/thumb/Purple114/v4/cf/18/67/cf1867cf-d21e-68d9-3d9b-f321a1a80207/mzl.imkvrcco.jpg/576x768bb.jpg",
                "https://is2-ssl.mzstatic.com/image/thumb/Purple114/v4/d6/e8/6c/d6e86cff-8620-4ffa-fa5d-93a253ab38df/mzl.bwmfmxug.jpg/576x768bb.jpg",
                "https://is2-ssl.mzstatic.com/image/thumb/Purple124/v4/fb/d1/c3/fbd1c331-04a0-122f-eea1-6304c452be6e/mzl.gxopfyrb.jpg/576x768bb.jpg"
            ],
            "appletvScreenshotUrls":[

            ],
            "artworkUrl60":"https://is2-ssl.mzstatic.com/image/thumb/Purple124/v4/a7/32/8c/a7328c6d-247e-578e-64fb-666ba3990947/source/60x60bb.jpg",
            "artworkUrl512":"https://is2-ssl.mzstatic.com/image/thumb/Purple124/v4/a7/32/8c/a7328c6d-247e-578e-64fb-666ba3990947/source/512x512bb.jpg",
            "artworkUrl100":"https://is2-ssl.mzstatic.com/image/thumb/Purple124/v4/a7/32/8c/a7328c6d-247e-578e-64fb-666ba3990947/source/100x100bb.jpg",
            "artistViewUrl":"https://apps.apple.com/cn/developer/wechat/id614694882?uo=4",
            "supportedDevices":[
                "iPhone5s-iPhone5s",
                "iPadAir-iPadAir",
                "iPadAirCellular-iPadAirCellular",
                "iPadMiniRetina-iPadMiniRetina",
                "iPadMiniRetinaCellular-iPadMiniRetinaCellular",
                "iPhone6-iPhone6",
                "iPhone6Plus-iPhone6Plus",
                "iPadAir2-iPadAir2",
                "iPadAir2Cellular-iPadAir2Cellular",
                "iPadMini3-iPadMini3",
                "iPadMini3Cellular-iPadMini3Cellular",
                "iPodTouchSixthGen-iPodTouchSixthGen",
                "iPhone6s-iPhone6s",
                "iPhone6sPlus-iPhone6sPlus",
                "iPadMini4-iPadMini4",
                "iPadMini4Cellular-iPadMini4Cellular",
                "iPadPro-iPadPro",
                "iPadProCellular-iPadProCellular",
                "iPadPro97-iPadPro97",
                "iPadPro97Cellular-iPadPro97Cellular",
                "iPhoneSE-iPhoneSE",
                "iPhone7-iPhone7",
                "iPhone7Plus-iPhone7Plus",
                "iPad611-iPad611",
                "iPad612-iPad612",
                "iPad71-iPad71",
                "iPad72-iPad72",
                "iPad73-iPad73",
                "iPad74-iPad74",
                "iPhone8-iPhone8",
                "iPhone8Plus-iPhone8Plus",
                "iPhoneX-iPhoneX",
                "iPad75-iPad75",
                "iPad76-iPad76",
                "iPhoneXS-iPhoneXS",
                "iPhoneXSMax-iPhoneXSMax",
                "iPhoneXR-iPhoneXR",
                "iPad812-iPad812",
                "iPad834-iPad834",
                "iPad856-iPad856",
                "iPad878-iPad878",
                "Watch4-Watch4",
                "iPadMini5-iPadMini5",
                "iPadMini5Cellular-iPadMini5Cellular",
                "iPadAir3-iPadAir3",
                "iPadAir3Cellular-iPadAir3Cellular",
                "iPodTouchSeventhGen-iPodTouchSeventhGen",
                "iPhone11-iPhone11",
                "iPhone11Pro-iPhone11Pro",
                "iPadSeventhGen-iPadSeventhGen",
                "iPadSeventhGenCellular-iPadSeventhGenCellular",
                "iPhone11ProMax-iPhone11ProMax",
                "iPhoneSESecondGen-iPhoneSESecondGen",
                "iPadProSecondGen-iPadProSecondGen",
                "iPadProSecondGenCellular-iPadProSecondGenCellular",
                "iPadProFourthGen-iPadProFourthGen",
                "iPadProFourthGenCellular-iPadProFourthGenCellular",
                "iPhone12Mini-iPhone12Mini",
                "iPhone12-iPhone12",
                "iPhone12Pro-iPhone12Pro",
                "iPhone12ProMax-iPhone12ProMax",
                "iPadAir4-iPadAir4",
                "iPadAir4Cellular-iPadAir4Cellular",
                "iPadEighthGen-iPadEighthGen",
                "iPadEighthGenCellular-iPadEighthGenCellular"
            ],
            "isGameCenterEnabled":false,
            "advisories":[
                "频繁/强烈的成人/性暗示题材"
            ],
            "kind":"software",
            "features":[
                "iosUniversal"
            ],
            "minimumOsVersion":"11.0",
            "trackCensoredName":"微信",
            "languageCodesISO2A":[
                "AR",
                "EN",
                "FR",
                "DE",
                "ID",
                "IT",
                "JA",
                "KO",
                "MS",
                "PT",
                "RU",
                "ZH",
                "ES",
                "TH",
                "ZH",
                "TR",
                "VI"
            ],
            "fileSizeBytes":"477456384",
            "sellerUrl":"http://weixin.qq.com",
            "formattedPrice":"免费",
            "contentAdvisoryRating":"17+",
            "averageUserRatingForCurrentVersion":4.36329999999999973425701682572253048419952392578125,
            "userRatingCountForCurrentVersion":5710077,
            "trackViewUrl":"https://apps.apple.com/cn/app/%E5%BE%AE%E4%BF%A1/id414478124?uo=4",
            "trackContentRating":"17+",
            "averageUserRating":4.36329999999999973425701682572253048419952392578125,
            "releaseDate":"2011-01-21T01:32:15Z",
            "trackId":414478124,
            "trackName":"微信",
            "currentVersionReleaseDate":"2021-02-02T08:15:22Z",
            "releaseNotes":"本次更新：
- 解决了一些已知问题。

最近更新：
- 更新了若干功能。",
            "primaryGenreName":"Social Networking",
            "genreIds":[
                "6005",
                "6007"
            ],
            "isVppDeviceBasedLicensingEnabled":true,
            "primaryGenreId":6005,
            "sellerName":"Tencent Technology (Shenzhen) Company Limited",
            "currency":"CNY",
            "version":"8.0.2",
            "wrapperType":"software",
            "artistId":614694882,
            "artistName":"WeChat",
            "genres":[
                "社交",
                "效率"
            ],
            "price":0,
            "description":"微信是一款全方位的手机通讯应用，帮助你轻松连接全球好友。微信可以群聊、进行视频聊天、与好友一起玩游戏，以及分享自己的生活到朋友圈，让你感受耳目一新的移动生活方式。

  为什么要使用微信：
  • 多媒体消息：支持发送视频、图片、文本和语音消息。
  • 群聊和通话：组建高达500人的群聊和高达9人的实时视频聊天。
  • 语音和视频聊天：提供全球的高质量通话。
  • 表情商店：海量动态表情，包括热门卡通人物和电影，让聊天变得更生动有趣。
  • 朋友圈：与好友分享每个精彩瞬间，记录自己的生活点滴。
  • 隐私保护：严格保护用户的隐私安全，是唯一一款通过TRUSTe认证的实时通讯应用。
  • 认识新朋友：通过“雷达加朋友”、“附近的人”和“摇一摇”认识新朋友。
  • 实时位置共享：与好友分享地理位置，无需通过语言告诉对方。
  • 多语言：支持超过20种语言界面，并支持多国语言的消息翻译。
  • 微信运动：支持接入Apple Watch及健康app数据，可在步数排行榜上和朋友一较高下。若需使用，可在“设置-通用-辅助功能”内启用。 
  • 更多功能: 支持跨平台、聊天室墙纸自定义、消息提醒自定义和公众号服务等。",
            "bundleId":"com.tencent.xin",
            "userRatingCount":5710077
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从App Store爬取了微信的基本信息，是一大堆<strong>json字符串</strong>，我们重点看这个字段：<code>"version":"8.0.2",</code>这个是App Store中的微信版本号，<strong>因为是App Store上面获取的，那么一定通过了审核，而且是最新的，而微信App通过iOS中的方法，是可以拿到本地版本号的。</strong></p>
<p>也就说，通过本地版本号和从App Store爬取的版本号对比，实现App添加版本升级功能。</p>
<p>Python可以通过rquest库获取数据，那么Swift必然也可以通过网络请求拿到相同的数据。</p>
<p>那么这个下面这个流程就能走通了：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b03b384c2737420cbc1773c83368b2ad~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>在App中通过Swift爬App Store信息 --> 返回App相关的json字符串 --> json字符串解析 --> 获取线上版本version--> 对比本地version --> 实现App版本升级功能</p>
</blockquote>
<p>思路梳理好了，下面实现起来，也就快了。</p>
<h3 data-id="heading-4">Swift代码实现逻辑</h3>
<ol>
<li>我们先通过上面的格式化的json，生成对应的模型，我非常喜欢使用Swift中原生自带的Codable协议解析json：</li>
</ol>
<pre><code class="copyable">/// 爬虫的数据模型
struct AppInfoAtStore: Codable &#123;
    let resultCount: Int?
    let results: [AppInfoResult]?
&#125;

/// 爬虫的详细数据模型
struct AppInfoResult: Codable &#123;
    let advisories: [String]?
    let appletvScreenshotUrls: [String]?
    let artistId: Int?
    let artistName: String?
    let artistViewUrl: String?
    let artworkUrl100: String?
    let artworkUrl512: String?
    let artworkUrl60: String?
    let averageUserRating: Float?
    let averageUserRatingForCurrentVersion : Float?
    let bundleId: String?
    let contentAdvisoryRating: String?
    let currency: String?
    let currentVersionReleaseDate: String?
    let descriptionField : String?
    let features: [String]?
    let fileSizeBytes: String?
    let formattedPrice: String?
    let genreIds: [String]?
    let genres: [String]?
    let ipadScreenshotUrls: [String]?
    let isGameCenterEnabled: Bool?
    let isVppDeviceBasedLicensingEnabled: Bool?
    let kind: String?
    let languageCodesISO2A: [String]?
    let minimumOsVersion: String?
    let price: Float?
    let primaryGenreId: Int?
    let primaryGenreName: String?
    let releaseDate: String?
    let releaseNotes: String?
    let screenshotUrls: [String]?
    let sellerName: String?
    let supportedDevices: [String]?
    let trackCensoredName: String?
    let trackContentRating: String?
    let trackId: Int?
    let trackName: String?
    let trackViewUrl: String?
    let userRatingCount: Int?
    let userRatingCountForCurrentVersion: Int?
    let version: String?
    let wrapperType: String?
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>通过Swift中的String类中的方法获取数据，然后通过Codable协议解析json为模型，返回需要的有效信息：</li>
</ol>
<pre><code class="copyable">/// 通过AppStore进行更新检查
/// 这个可以看成是一个请求,也可以看成是一个爬虫
/// - Parameter appleId: App Store Connect页面 App信息 综合信息的 Apple Id
/// - Returns: AppStore中的版本信息 本地版本信息 是否需要升级 Bool值 true表示需要升级 升级网址
public func checkAppStoreVersion(appleId: String) -> (appStoreVersion: String?, localVersion: String?, isNeedUpdate: Bool, updateURL: String?) &#123;
    guard let url = URL(string: "http://itunes.apple.com/cn/lookup?id=\(appleId)"),
        let jsonResponseString =  try? String(contentsOf: url, encoding: String.Encoding.utf8),
        let data = jsonResponseString.data(using: .utf8) else &#123;
            return (nil, nil, false, nil)
    &#125;

    /// Codable协议解析
    let appInfoAtStore = try? JSONDecoder().decode(AppInfoAtStore.self, from: data)

    /// appStore中的版本号
    let appStoreVersion = appInfoAtStore?.results?.first?.version

    /// 本地版本号
    let localVersion = Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String


    guard let aVersion = appStoreVersion, let lVersion = localVersion else &#123;
        return (nil, nil, false, nil)
    &#125;

    /// 是否需要更新
    let isNeedUpdate = aVersion.compare(lVersion).rawValue > 0

    /// 需要跳转更新的地址
    let updateURL = appInfoAtStore?.results?.first?.trackViewUrl

    /// 返回元组信息
    return (aVersion, lVersion, isNeedUpdate, updateURL)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此，通过App Store获取版本信息，完成App版本升级功能的基本完成了。</p>
<h2 data-id="heading-5">思考总结</h2>
<h3 data-id="heading-6">思考</h3>
<p>在完成上面的代码，并测试后，我也想了下面一些问题，下面的观点仅仅是我的理解，希望大家能思考互动一下：</p>
<ol>
<li>Alamofire可以干爬虫这事么？</li>
</ol>
<blockquote>
<p>答：本质上爬虫也是网络请求，所以Alamofire也可以胜任此工作。</p>
</blockquote>
<ol start="2">
<li>这种方式爬取的version可以控制强制升级么？</li>
</ol>
<blockquote>
<p>答：如果定好规则，是可以的。比如版本号是X.Y.Z这样，用X，Y位的大小判断是否需要强制升级即可。</p>
</blockquote>
<ol start="3">
<li>这种方式可以规避App在审核过程中提示升级么？</li>
</ol>
<blockquote>
<p>答：可以的，因为在审核过程中，App Store中还没有上架，此时lVersion大于aVersion，isNeedUpdate为false，不会触发升级。</p>
</blockquote>
<ol start="4">
<li>这种方式有什么风险点？</li>
</ol>
<blockquote>
<p>答：这个url是苹果提供，苹果会不会停止对外暴露这个接口，这个事情我们说了不算，所以还是存在一定的风险的。最好的还是通过App后台控制。</p>
</blockquote>
<h3 data-id="heading-7">总结</h3>
<p>App后台不提供数据支撑，而这个数据又必须网络请求获取到，那么我们可不可以换个源试试？有没有现成网站或者接口支持该操作的？</p>
<p>虽然这种场景不常见（后台如果说App版本管理做不了，就拿砖头pia飞），但是正是因为思考所以才有了这次尝试。</p>
<p>很多人都不太喜欢用Swift中Codable协议做json转model，孰不知原生的这种方式其实挺好用的，从Alamofire5开始已经原生支持Codable协议解析json了。</p>
<p>元组其实是个好东西，这个从Python借鉴的类型，在较少数据的时候，也有发挥的时候。</p>
<p>Swift中的Data类中也有一个方法，可以直接爬数据为二进制，可以去试试喔。</p>
<h3 data-id="heading-8">注意事项</h3>
<p>刚刚查阅了一下资料，其实发现一些特别要注意的地方，因为使用的搜索微信App信息作为例子，忽略了一些细节：</p>
<p><strong>如果你的应用是在全世界范围内销售的话, 用上面的是没问题的但是，如果仅仅是在部分地区，比如只在中国商店提供下载，就需要在路径是加上国家的缩写cn。</strong></p>
<p><strong><code>http://itunes.apple.com/cn/lookup?id=appId </code>(appId为应用 id)</strong></p>
<p><strong>否则你将会得到一个 results : [] 的结果。</strong></p>
<blockquote>
<p>参考资料：<a href="https://www.jianshu.com/p/aad031a0bb52" target="_blank" rel="nofollow noopener noreferrer">iOS获取 App详细信息的方法</a></p>
</blockquote>
<p>本文正在参与「掘金 2021 春招闯关活动」, 点击查看<a href="https://juejin.cn/post/6933147477399109640" target="_blank">活动详情</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            