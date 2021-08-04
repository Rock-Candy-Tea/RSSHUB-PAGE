
---
title: 'iOS 识别虚拟定位调研'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/794fa4da8b2a40d1925cc68375927d69~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 05:00:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/794fa4da8b2a40d1925cc68375927d69~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近业务开发中，有遇到我们的项目app定位被篡改的情况，在android端表现的尤为明显。为了防止这种黑产使用虚拟定位薅羊毛，iOS也不得不进行虚拟定位的规避。
在做技术调研后，发现在苹果手机上，单凭一部手机，真正要实现虚拟定位，是比较难实现的，但还是有存在的可能性，公司的一个项目app的bugly记录反馈用户存在使用越狱苹果手机，这就着实让人这种行为实在有大嫌。
本人和公司伙伴的共同努力下，大致调研了以下使用虚拟定位的情况(使用Xcode虚拟定位的方式本文忽略)：</p>
<p>第一种：使用越狱手机。</p>
<p>一般app用户存在使用越狱苹果手机的情况，一般可以推断用户的行为存在薅羊毛的嫌疑（也有app被竞品公司做逆向分析的可能），因为买一部越狱的手机比买一部正常的手机有难度，且在系统升级和appstore的使用上，均不如正常手机，本人曾经浅浅的接触皮毛知识通过越狱iPhone5s进行的app逆向。</p>
<p>识别方式：</p>
<p>建议一刀切的方式进行，通过识别手机是否安装了Cydia.app,如果安装了直接判定为越狱手机，并向后台上报“设备异常”的信息。如果不使用这种方式的方式，请继续看，后面会有其他方式解决。专业的逆向人员是绝对可以避免app开发者对Cydia的安装检测的，当然这种情况是app在市场上有很大的份量，被竞争对手拿来进行逆向分析，对这种情况，虚拟的识别基本毫无意义。个人建议，直接锁死停掉此手机app的接口服务。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.huaweicloud.com%2Farticles%2F7c6b8027253c4a97196d359840f638d9.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.huaweicloud.com/articles/7c6b8027253c4a97196d359840f638d9.html" ref="nofollow noopener noreferrer">这里推荐一篇开发者如何识别苹果手机已经越狱的文章</a>。</p>
<p>代码实现：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">/// 判断是否是越狱设备</span>
<span class="hljs-comment">/// - Returns: true 表示设备越狱</span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">isBrokenDevice</span>()</span> -> <span class="hljs-type">Bool</span> &#123;
    
    <span class="hljs-keyword">var</span> isBroken <span class="hljs-operator">=</span> <span class="hljs-literal">false</span>
    
    <span class="hljs-keyword">let</span> cydiaPath <span class="hljs-operator">=</span> <span class="hljs-string">"/Applications/Cydia.app"</span>
    
    <span class="hljs-keyword">let</span> aptPath <span class="hljs-operator">=</span> <span class="hljs-string">"/private/var/lib/apt"</span>
    
    <span class="hljs-keyword">if</span> <span class="hljs-type">FileManager</span>.default.fileExists(atPath: cydiaPath) &#123;
        isBroken <span class="hljs-operator">=</span> <span class="hljs-literal">true</span>
    &#125;
    
    <span class="hljs-keyword">if</span> <span class="hljs-type">FileManager</span>.default.fileExists(atPath: aptPath) &#123;
        isBroken <span class="hljs-operator">=</span> <span class="hljs-literal">true</span>
    &#125;
    
    <span class="hljs-keyword">return</span> isBroken
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二种：使用爱思助手。</p>
<p>对于使用虚拟定位的场景，大多应该是司机或对接人员打卡了。而在这种场景下，就可能催生了一批专门以使用虚拟定位进行打卡薅羊毛的黑产。对于苹果手机，目前而言，能够很可以的实现的，当数爱思助手的虚拟定位功能了。</p>
<p>使用步骤：下载爱思助手mac客户端，连接苹果手机，工具箱中点击虚拟定位，即可在地图上选定位，然后点击修改虚拟定位即可实现修改地图的定位信息。</p>
<p>原理：在未越狱的设备上通过电脑和手机进行USB连接，电脑通过特殊协议向手机上的DTSimulateLocation服务发送模拟的坐标数据来实现虚假定位，目前Xcode上内置位置模拟就是借助这个技术来实现的。（ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fdeveloper%2Farticle%2F1800531" target="_blank" rel="nofollow noopener noreferrer" title="https://cloud.tencent.com/developer/article/1800531" ref="nofollow noopener noreferrer">文章来源</a>）</p>
<p>识别方式：</p>
<p>一、通过多次记录爱思助手的虚拟定位的数据发现，其虚拟的定位信息的经纬度的高度是为0且经纬度的数据位数也是值得考究的。真实定位和虚拟定位数据如下图：</p>
<p>真实定位
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/794fa4da8b2a40d1925cc68375927d69~tplv-k3u1fbpfcp-watermark.image" alt="真实定位.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>虚拟定位
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dfb1207c7a74995903c4b326845f53e~tplv-k3u1fbpfcp-watermark.image" alt="虚拟定位.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>仔细观察数据，不难发现，如果我们比对获取定位信息的高度，以及对经纬度的double位数也进行校验，虚拟定位的黑帽子就会轻易被破了。那么如果我们比对虚拟定位的高度为0时，就认定为虚拟定位，那么就会产生一个疑问，真实海拔就是零的地点，如何解决？这里科普下中国的海拔零度位置，中国水准零点位于青岛市东海中路银海大世界内的“中华人民共和国水准零点”，是国内唯一的水准零点。唯一的水准零点。同时，因为比对经纬度的double位数，发现虚拟定位的位数很明显不对，核对swift的float和double的位数精度发现，虚拟定位的经纬度数据只是敷衍的满足double精度位数，swift的float有效位数是7，double的有效位数是15。当然这个比较的权重是相对高度比较低的，笔者刚刚更新爱思助手版本发现新版本经纬度有更详细，但是还是达不到double的有效位数级别。相对于目前的爱思助手的高度比较识别为虚拟定位，已经完全可以做到</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba2a7e7daa5b4d4d857b011d4ce8840d~tplv-k3u1fbpfcp-watermark.image" alt="精度.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码实现：</p>
<pre><code class="copyable">       if location.altitude == 0.0 &#123;
            print("虚拟定位")
        &#125;

        //位数作为判定的权重比，如果位数小于12(假定值,目前爱思助手的虚拟定位的此数据的位数是9)，判断为虚拟定位，
        //危险慎用，但是作为小权重的异常数据记录还是可以的
        let longitude = location.coordinate.longitude
        let longitudeStr = "\(longitude)".components(separatedBy: ".").last ?? ""

        print("经度的有效位数：\(longitudeStr.count)")
        if longitudeStr.count < 12 &#123;

            print("虚拟定位")
        &#125;
                
<span class="copy-code-btn">复制代码</span></code></pre>
<p>二、把定位后的数据的经纬度上传给后台，后台再根据收到的经纬度获取详细的经纬度信息，对司机的除经纬度以外的地理信息进行深度比较，优先比较altitude、horizontalAccuracy、verticalAccuracy值，根据值是否相等进行权衡后，确定。</p>
<p>三、</p>
<p>（一）通过获取公网ip，大概再通过接口根据ip地址可获取大概的位置，但误差范围有点大。</p>
<pre><code class="hljs language-获取ip地址 copyable" lang="获取ip地址">    //获取公网ip地址
    var ipAddress: String? &#123;
        
        let ipUrl = URL(string: "https://ipof.in/txt")!
        let ip = try? String.init(contentsOf: ipUrl, encoding: .utf8)

        return ip
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（二）<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.caojiarun.com%2F2017%2F01%2FiOS_Wifilist%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.caojiarun.com/2017/01/iOS_Wifilist/" ref="nofollow noopener noreferrer">通过Wi-Fi热点来读取app位置</a></p>
<p>（三）利用CLCircularRegion设定区域中心的指定经纬度和可设定半径范围，进行监听。</p>
<p>代码简略实现：</p>
<pre><code class="copyable">
    manager = CLLocationManager()
    //设置定位服务管理器代理
    manager?.delegate = self
    //设置定位模式
    manager?.desiredAccuracy = kCLLocationAccuracyBest
    //更新距离
    manager?.distanceFilter = 100
    //发送授权申请
    manager?.requestWhenInUseAuthorization()

    let latitude = 115.47560123242931
    let longitude = 29.9757535600194
    let centerCoordinate = CLLocationCoordinate2D(latitude: latitude, longitude: longitude)
    let locationIDStr = ""
    let clRegion = CLCircularRegion(center: centerCoordinate, radius: 100, identifier: locationIDStr)
    manager?.startMonitoring(for: clRegion)
    
    代理方法
    
     func locationManager(_ manager: CLLocationManager, didEnterRegion region: CLRegion) &#123;
        
    &#125;
    
    func locationManager(_ manager: CLLocationManager, didExitRegion region: CLRegion) &#123;
        
    &#125;
    
    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（四）通过IBeacon技术，使用 CoreBluetooth 框架下的CBPeripheralManager建立一个蓝牙基站。这种定位直接是端对端的直接定位，省去了GPS的卫星和蜂窝数据的基站通信。</p>
<p>代码简略实现：</p>
<pre><code class="copyable">func locationManager(_ manager: CLLocationManager, didRangeBeacons beacons: [CLBeacon], in region: CLBeaconRegion) &#123;

    for beacon in beacons &#123;
        var proximityStr: String = ""
        switch beacon.proximity &#123;
        case .far:
            proximityStr = "Unknown"
        case .immediate:
            proximityStr = "Immediate"
        case .near:
            proximityStr = "Near"
        case .unknown:
            proximityStr = "Unknown"
        &#125;

        var beaconStr = "信号：" + beacon.proximityUUID.uuidString + "major:" + beacon.major.stringValue + "minor:" + beacon.minor.stringValue + "距离：" + beacon.accuracy + "信号：" + "\(Int64(beacon.rssi))" + "接近度：" + proximityStr

        print("beacon信息: \(beaconStr)")
    &#125;

&#125;

func locationManager(_ manager: CLLocationManager, rangingBeaconsDidFailFor region: CLBeaconRegion, withError error: Error) &#123;

&#125;
    
----------------------------------------------------------------------------------

//不能单独创建一个类遵守CBPeripheralManagerDelegate协议，需要先遵守NSObjectProtocol协议，这里直接继承NSObject
class CoreBluetoothManager:NSObject, CBPeripheralManagerDelegate &#123; 
    
    //建立一个蓝牙基站。
    lazy var peripheralManager: CBPeripheralManager =  CBPeripheralManager(delegate: self, queue: DispatchQueue.main, options: nil)
            
    lazy var region: CLBeaconRegion = &#123;
        
        guard let uuid = UUID(uuidString: "xxx") else &#123;
            return CLBeaconRegion()
        &#125;
        let major: CLBeaconMajorValue = 1
        let minor: CLBeaconMajorValue = 1
        let id = "创建的蓝牙基站的名称"
        let region = CLBeaconRegion(proximityUUID: uuid, major: major, minor: minor, identifier: id)
        return region
    &#125;()
    
    func peripheralManagerDidUpdateState(_ peripheral: CBPeripheralManager) &#123;
        
        switch peripheral.state &#123;
        case CBManagerState.poweredOn:
            
            if let data = self.region.peripheralData(withMeasuredPower: nil) as? [String : Any] &#123;
                
                self.peripheralManager.startAdvertising(data)
            &#125;
            
        case CBManagerState.poweredOff,
             CBManagerState.resetting,
             CBManagerState.unauthorized,
             CBManagerState.unsupported,
             CBManagerState.unknown:
            
            break
        &#125;
    &#125;
   
    func peripheralManagerDidStartAdvertising(_ peripheral: CBPeripheralManager, error: Error?) &#123;
        
    &#125;
        
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>四（待完善）、
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fdeveloper%2Farticle%2F1800531" target="_blank" rel="nofollow noopener noreferrer" title="https://cloud.tencent.com/developer/article/1800531" ref="nofollow noopener noreferrer">此文章</a>的末尾附的解法本人有尝试过，一层一层通过kvc读取CLLocation的_internal的fLocation，只能读取到到此。再通过kvc读取会报以下错误：</p>
<pre><code class="copyable">Expression can't be run, because there is no JIT compiled function
<span class="copy-code-btn">复制代码</span></code></pre>
<p>深入研究，在苹果的官方开发文档上发现了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fbundleresources%2Fentitlements%2Fcom_apple_security_cs_allow-jit" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_cs_allow-jit" ref="nofollow noopener noreferrer">这个解释</a>，也有说设置debug+优化策略的，但iOS默认bug环境就是-Onone级别的。其实主要原因貌似因为JIT的设置是在开发mac客户端的时候，才能在Signing&Capabilities的Hardened Runtime中找到。关于Allow Execution of JIT-compiled Code的设置（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fsecurity%2Fhardened_runtime" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/security/hardened_runtime" ref="nofollow noopener noreferrer">官方文章</a>）。最终只能卡到这里，若有大神能通过其他方式读取CLLocation的真实定位（这是极其完美的解决方案），还请不吝赐教。</p>
<p>附：</p>
<p>CLLocation对象私有变量<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnst%2FiOS-Runtime-Headers%2Fblob%2Fmaster%2FFrameworks%2FCoreLocation.framework%2FCLLocationInternal.h" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nst/iOS-Runtime-Headers/blob/master/Frameworks/CoreLocation.framework/CLLocationInternal.h" ref="nofollow noopener noreferrer">_internal实例对象的官方定义</a>：</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-meta">@interface</span> <span class="hljs-type">CLLocationInternal</span> : <span class="hljs-type">NSObject</span> &#123;
    <span class="hljs-class"><span class="hljs-keyword">struct</span> </span>&#123;
        int suitability;
        <span class="hljs-class"><span class="hljs-keyword">struct</span> </span>&#123;
            double latitude;
            double longitude;
        &#125; coordinate;
        double horizontalAccuracy;
        double altitude;
        double verticalAccuracy;
        double speed;
        double speedAccuracy;
        double course;
        double courseAccuracy;
        double timestamp;
        int confidence;
        double lifespan;
        int type;
        <span class="hljs-class"><span class="hljs-keyword">struct</span> </span>&#123;
            double latitude;
            double longitude;
        &#125; rawCoordinate;
        double rawCourse;
        int floor;
        unsigned int integrity;
        int referenceFrame;
        int rawReferenceFrame;
    &#125;  fLocation;
    <span class="hljs-type">CLLocationMatchInfo</span> <span class="hljs-operator">*</span> fMatchInfo;
    double  fTrustedTimestamp;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-Objc copyable" lang="Objc">
<span class="hljs-class"><span class="hljs-keyword">@class</span> <span class="hljs-title">NSData</span>;</span>

<span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">CLLocationMatchInfo</span> : <span class="hljs-title">NSObject</span> <<span class="hljs-title">NSCopying</span>, <span class="hljs-title">NSSecureCoding</span>> </span>&#123;

    <span class="hljs-keyword">id</span> _internal;
&#125;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>,<span class="hljs-keyword">readonly</span>) <span class="hljs-keyword">long</span> <span class="hljs-keyword">long</span> matchQuality;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>,<span class="hljs-keyword">readonly</span>) <span class="hljs-built_in">CLLocationCoordinate2D</span> matchCoordinate;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>,<span class="hljs-keyword">readonly</span>) <span class="hljs-keyword">double</span> matchCourse;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>,<span class="hljs-keyword">readonly</span>) <span class="hljs-keyword">int</span> matchFormOfWay;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>,<span class="hljs-keyword">readonly</span>) <span class="hljs-keyword">int</span> matchRoadClass;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">getter</span>=isMatchShifted,<span class="hljs-keyword">nonatomic</span>,<span class="hljs-keyword">readonly</span>) <span class="hljs-built_in">BOOL</span> matchShifted;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>,<span class="hljs-keyword">copy</span>,<span class="hljs-keyword">readonly</span>) <span class="hljs-built_in">NSData</span> * matchDataArray;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            