
---
title: 'iOS - 使用UIStackView构建分享面板'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a46d6f5987b4057b3e9c30818f7f9b6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 01:05:54 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a46d6f5987b4057b3e9c30818f7f9b6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>最近我们iOS适配可以放弃iOS8了（喜大普奔）。想想也是，连微信最新版本都要求使用iOS11版本了。于是我们可以热情的使用iOS9之后的控件了。例如：UIStackView</p>
<p>UIStackView继承自UIView，用来管理在它内部的views，确实可以很大程度提高界面开发效率，每一个iOS开发者都应该熟练掌握UIStackView的使用。</p>
<h2 data-id="heading-1">二、效果</h2>
<h3 data-id="heading-2">1、UIStackView + UIScrollow 的效果</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a46d6f5987b4057b3e9c30818f7f9b6~tplv-k3u1fbpfcp-watermark.image" alt="QQ20210702-152244-HD.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2、UIStackView 单独效果</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd5c26ed7dac4751bf44be0e8e44256a~tplv-k3u1fbpfcp-watermark.image" alt="QQ20210702-152642-HD.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">三、项目描述</h2>
<p>项目代码比较通俗易懂，布局使用了 SnapKit 。</p>
<h3 data-id="heading-5">枚举类型</h3>
<p>因为我们是分享面板，枚举类型是必不可少的类型，我们定义了分享平台的枚举，以及分享样式的枚举</p>
<pre><code class="copyable">//分享平台枚举
public enum LGSharePlateformEnum: String &#123;
    case wechat = "微信"
    case wechatTimeline = "朋友圈"
    case qqFriend = "QQ"
    case qqZone = "QQ空间"
    case dingTalk = "钉钉"
    case none = ""

    public func info() -> (title: String?, icon: UIImage?) &#123;

        switch self &#123;
        case .wechat:
            return ("微信", UIImage(named: "nav_share_weixin"))
        case .qqFriend:
            return ("QQ", UIImage(named: "nav_share_qq"))
        case .wechatTimeline:
            return ("朋友圈", UIImage(named: "nav_share_pengyouquan")
        case .qqZone:
            return ("QQ空间", UIImage(named: "nav_share_kaliao_qqzone"))
        case .dingTalk:
            return ("钉钉", UIImage(named: "nav_share_dingding"))
        case .none:
            return (nil, nil)
        &#125;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//分享样式枚举
public enum LGShareTypeEnum &#123;
    case normal
    case scrollow
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>1、因为我们使用swift开发，枚举可以定义字符串类型枚举，甚至可以调用方法，极大的便利了我们的开发效率</p>
<p>2、分享平台枚举我们定义了.none的枚举，是因为UIStackView的特性，用空元素补齐。</p>
<h3 data-id="heading-6">单行的可滑动的分享面板</h3>
<pre><code class="copyable">public class LGShareScrollView: UIView &#123;

    var didSelectItem: ((_ plateform: LGSharePlateformEnum?) -> Void)?
    //平台分享
    lazy var platformStackView: UIStackView = &#123;
        let stackView = UIStackView()
        stackView.spacing = 25
        stackView.isUserInteractionEnabled = true
        stackView.axis = .horizontal
        stackView.distribution = .equalSpacing
        return stackView
    &#125;()

    var plateform: [LGSharePlateformEnum]? &#123;
        didSet &#123;
            for plateItem in plateform ?? [] &#123;
                let itemView = LGShareItemView()
                itemView.didSelectItem = didSelectItem
                itemView.sharePlateform = plateItem
                platformStackView.addArrangedSubview(itemView)
                itemView.snp.makeConstraints &#123; (make) in
                    make.height.equalTo(100)
                    make.width.equalTo(50)
                &#125;
            &#125;

        &#125;
    &#125;

    private var scrollow: UIScrollView?

    public var safeBottomHeight: CGFloat &#123;
        var bottomH: CGFloat = 0.0
        if #available(iOS 11.0, *) &#123;
            bottomH = UIApplication.shared.delegate?.window??.safeAreaInsets.bottom ?? 0
        &#125;
        return bottomH
    &#125;


    override init(frame: CGRect) &#123;
        super.init(frame: frame)
        setupStackView()

    &#125;

    override public func layoutSubviews() &#123;
        super.layoutSubviews()
        let stackViewWidth = platformStackView.frame.size.width
        scrollow?.contentSize = CGSize(width: stackViewWidth + 30, height: 0)
    &#125;

    func setupStackView() &#123;
        self.isUserInteractionEnabled = true
        let scrollow = UIScrollView()
        scrollow.showsHorizontalScrollIndicator = false
        self.scrollow = scrollow
        scrollow.isUserInteractionEnabled = true
        self.addSubview(scrollow)
        scrollow.snp.makeConstraints &#123; (make) in
            make.top.left.right.equalToSuperview()
            make.height.equalTo(100)
            make.bottom.equalToSuperview().offset(-safeBottomHeight)
        &#125;

        scrollow.addSubview(platformStackView)

        platformStackView.snp.makeConstraints &#123; (make) in
            make.top.bottom.equalToSuperview()
            make.left.equalToSuperview().offset(15)
            make.height.equalTo(100)
        &#125;

    &#125;

    required init?(coder: NSCoder) &#123;
        fatalError("init(coder:) has not been implemented")
    &#125;

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>1、使用 UIScrollView + UIStackView 的方式</p>
<p>2、设置UIStackView的上、左、下、高度，snapKit的 AutoLayout 会自动计算宽度</p>
<p>3、在layoutSubviews里要设置scrollow.contentSize，否则不能滑动</p>
<h3 data-id="heading-7">可自动换行的分享面板</h3>
<pre><code class="copyable">public class LGShareStackView: UIView &#123;

    var didSelectItem: ((_ plateform: LGSharePlateformEnum?) -> Void)?

    var lineNumber = 5
    //纵向的
    lazy var platformStackView: UIStackView = &#123;
        let stackView = UIStackView()
        stackView.isUserInteractionEnabled = true
        stackView.axis = .vertical
        stackView.distribution = .fillEqually
        return stackView
    &#125;()

    var plateform: [LGSharePlateformEnum]? &#123;
        didSet &#123;

            let line = (((plateform?.count ?? 0) - 1) / lineNumber) + 1
            for i in 0..<line &#123;
                let stackView = UIStackView()
                stackView.isUserInteractionEnabled = true
                stackView.axis = .horizontal
                stackView.distribution = .fillEqually
                platformStackView.addArrangedSubview(stackView)
                stackView.snp.makeConstraints &#123; (make) in
                    make.left.right.equalToSuperview()
                    make.height.equalTo(100)
                &#125;
                for j in 0..<lineNumber &#123;
                    let plateItem = (((i * lineNumber) + j) < plateform?.count ?? 0) ? plateform?[((i * lineNumber) + j)] : LGSharePlateformEnum.none
                    let itemView = LGShareItemView()
                    itemView.didSelectItem = didSelectItem
                    itemView.sharePlateform = plateItem
                    stackView.addArrangedSubview(itemView)
                    itemView.snp.makeConstraints &#123; (make) in
                        make.height.equalTo(100)
                        make.top.equalToSuperview()
                    &#125;
                &#125;
            &#125;

        &#125;
    &#125;

    public var safeBottomHeight: CGFloat &#123;
        var bottomH: CGFloat = 0.0
        if #available(iOS 11.0, *) &#123;
            bottomH = UIApplication.shared.delegate?.window??.safeAreaInsets.bottom ?? 0
        &#125;
        return bottomH
    &#125;


    override init(frame: CGRect) &#123;
        super.init(frame: frame)
        setupStackView()

    &#125;

    func setupStackView() &#123;
        self.isUserInteractionEnabled = true
        self.addSubview(platformStackView)
        platformStackView.snp.makeConstraints &#123; (make) in
            make.top.left.right.equalToSuperview()
            make.bottom.equalToSuperview().offset(-safeBottomHeight)
        &#125;
    &#125;

    required init?(coder: NSCoder) &#123;
        fatalError("init(coder:) has not been implemented")
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1、逻辑是一个纵向的UIStackView，套着多个横向的UIStackView
2、可以设置行数个数来设置每行的个数</p>
<p>如图所示</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b10a60616514c90b9c62ab0cbc4a755~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-02 下午4.50.03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">四、最后</h2>
<p>iOS9之后 使用UIStackView，不用考虑views坐标，类似安卓的线性布局。使用非常舒服，方便。
项目github地址 ：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FQinzhao%2FLGShareViewTool" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Qinzhao/LGShareViewTool" ref="nofollow noopener noreferrer">github.com/Qinzhao/LGS…</a></p></div>  
</div>
            