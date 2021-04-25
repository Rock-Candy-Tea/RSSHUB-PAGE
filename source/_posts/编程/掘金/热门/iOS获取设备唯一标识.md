
---
title: 'iOS获取设备唯一标识'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfc22a8459c4481199377fec9d550c5c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 21 Apr 2021 23:36:40 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfc22a8459c4481199377fec9d550c5c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 常用的UUID</h2>
<p>UDID是一个40位十六进制序列（越狱的设备通过某些工具可以改变设备的 UDID），移动网络可以利用 UDID 来识别移动设备。</p>
<p>许多开发者把 UDID 跟用户的个人信息关联起来，网络窥探者会从多个应用收集这些数据，然后顺藤摸瓜得到这个人的许多隐私数据，同时大部分应用确实在频繁传输 UDID 和私人信息。 为了避免集体诉讼，苹果最终决定在 iOS 5 的时候，将这一惯例废除。</p>
<ul>
<li>获取UUID的方法：</li>
</ul>
<pre><code class="hljs language-oc copyable" lang="oc">/**  卸载应用重新安装后会不一致*/
+ (NSString *)getUUID&#123;
    return [UIDevice currentDevice].identifierForVendor.UUIDString;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. MAC 地址</h2>
<p>MAC地址，用来表示互联网上每一个站点的标示符，是一个六个字节（48位）的十六进制序列。前三个字节是由 IEEE 的注册管理机构 RA 负责给不同厂家分配的”编制上唯一的标示符，后三个字节由各厂家自行指派给生产的适配器接口。</p>
<p>MAC 地址在网络上用来区分设备的唯一性，接入网络的设备都有一个MAC地址，他们肯定都是唯一的。一部 iPhone 上可能有多个 MAC 地址，包括 WIFI 的、SIM 的等，但是 iTouch 和 iPad 上就有一个 WIFI 的，因此只需获取 WIFI 的 MAC 地址就好了。一般会采取 MD5（MAC 地址 + bundleID）获取唯一标识。</p>
<p>但是 MAC 地址和 UDID 一样，存在隐私问题， iOS 7 之后，所有设备请求 MAC 地址会返回一个固定值，这个方法也不攻自破了。</p>
<p>获取MAC在github找到一个挺好的方法：</p>
<h3 data-id="heading-2">2.1  首先导入下面几个库：</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfc22a8459c4481199377fec9d550c5c~tplv-k3u1fbpfcp-watermark.image" alt="1619074874524.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2.2 新建一个文件，继承NSObject,在.m文件导入头文件，以及定义一些宏</h3>
<pre><code class="hljs language-oc copyable" lang="oc">#import "XWGetMAC.h"
#import <ifaddrs.h>
#import <resolv.h>
#import <arpa/inet.h>
#import <net/if.h>
#import <netdb.h>
#import <netinet/ip.h>
#import <net/ethernet.h>
#import <net/if_dl.h>

#define MDNS_PORT       5353
#define QUERY_NAME      "_apple-mobdev2._tcp.local"
#define DUMMY_MAC_ADDR  @"02:00:00:00:00:00"
#define IOS_CELLULAR    @"pdp_ip0"
#define IOS_WIFI        @"en0"
#define IOS_VPN         @"utun0"
#define IP_ADDR_IPv4    @"ipv4"
#define IP_ADDR_IPv6    @"ipv6"
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-oc copyable" lang="oc">+ (NSString *)getMAC:(BOOL)preferIPv4 &#123;
    
    return [[XWGetMAC alloc] getIPAddress:preferIPv4];
&#125;

/*
 * 获取设备当前网络IP地址
 */
- (NSString *)getIPAddress:(BOOL)preferIPv4
&#123;
    NSArray *searchArray = preferIPv4 ?
    @[ IOS_VPN @"/" IP_ADDR_IPv4, IOS_VPN @"/" IP_ADDR_IPv6, IOS_WIFI @"/" IP_ADDR_IPv4, IOS_WIFI @"/" IP_ADDR_IPv6, IOS_CELLULAR @"/" IP_ADDR_IPv4, IOS_CELLULAR @"/" IP_ADDR_IPv6 ] :
    @[ IOS_VPN @"/" IP_ADDR_IPv6, IOS_VPN @"/" IP_ADDR_IPv4, IOS_WIFI @"/" IP_ADDR_IPv6, IOS_WIFI @"/" IP_ADDR_IPv4, IOS_CELLULAR @"/" IP_ADDR_IPv6, IOS_CELLULAR @"/" IP_ADDR_IPv4 ] ;
    
    NSDictionary *addresses = [self getIPAddr];
    
    __block NSString *address;
    [searchArray enumerateObjectsUsingBlock:^(NSString *key, NSUInteger idx, BOOL * _Nonnull stop) &#123;
        address = addresses[key];
        //筛选出IP地址格式
        if([self isValidatIP:address]) *stop = YES;
    &#125;];
    return address ? address : @"0.0.0.0";
&#125;

- (BOOL)isValidatIP:(NSString *)ipAddress &#123;
    if (ipAddress.length == 0) &#123;
        return NO;
    &#125;
    NSString *urlRegEx = @"^([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\."
    "([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\."
    "([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\."
    "([01]?\\d\\d?|2[0-4]\\d|25[0-5])$";
    
    NSError *error;
    NSRegularExpression *regex = [NSRegularExpression regularExpressionWithPattern:urlRegEx options:0 error:&error];
    
    if (regex != nil) &#123;
        NSTextCheckingResult *firstMatch=[regex firstMatchInString:ipAddress options:0 range:NSMakeRange(0, [ipAddress length])];
        return firstMatch;
    &#125;
    return NO;
&#125;

- (NSDictionary *)getIPAddr
&#123;
    NSMutableDictionary *addresses = [NSMutableDictionary dictionaryWithCapacity:8];
    
    // retrieve the current interfaces - returns 0 on success
    struct ifaddrs *interfaces;
    if(!getifaddrs(&interfaces)) &#123;
        // Loop through linked list of interfaces
        struct ifaddrs *interface;
        for(interface=interfaces; interface; interface=interface->ifa_next) &#123;
            if(!(interface->ifa_flags & IFF_UP) /* || (interface->ifa_flags & IFF_LOOPBACK) */ ) &#123;
                continue; // deeply nested code harder to read
            &#125;
            const struct sockaddr_in *addr = (const struct sockaddr_in*)interface->ifa_addr;
            char addrBuf[ MAX(INET_ADDRSTRLEN, INET6_ADDRSTRLEN) ];
            if(addr && (addr->sin_family==AF_INET || addr->sin_family==AF_INET6)) &#123;
                NSString *name = [NSString stringWithUTF8String:interface->ifa_name];
                NSString *type;
                if(addr->sin_family == AF_INET) &#123;
                    if(inet_ntop(AF_INET, &addr->sin_addr, addrBuf, INET_ADDRSTRLEN)) &#123;
                        type = IP_ADDR_IPv4;
                    &#125;
                &#125; else &#123;
                    const struct sockaddr_in6 *addr6 = (const struct sockaddr_in6*)interface->ifa_addr;
                    if(inet_ntop(AF_INET6, &addr6->sin6_addr, addrBuf, INET6_ADDRSTRLEN)) &#123;
                        type = IP_ADDR_IPv6;
                    &#125;
                &#125;
                if(type) &#123;
                    NSString *key = [NSString stringWithFormat:@"%@/%@", name, type];
                    addresses[key] = [NSString stringWithUTF8String:addrBuf];
                &#125;
            &#125;
        &#125;
        // Free memory
        freeifaddrs(interfaces);
    &#125;
    return [addresses count] ? addresses : nil;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-oc copyable" lang="oc">/*
 * 获取设备物理地址
 */
- (nullable NSString *)getMacAddress &#123;
    res_9_init();
    int len;
    //get currnet ip address
    NSString *ip = [self currentIPAddressOf:IOS_WIFI];
    if(ip == nil) &#123;
        fprintf(stderr, "could not get current IP address of en0\n");
        return DUMMY_MAC_ADDR;
    &#125;//end if
    
    //set port and destination
    _res.nsaddr_list[0].sin_family = AF_INET;
    _res.nsaddr_list[0].sin_port = htons(MDNS_PORT);
    _res.nsaddr_list[0].sin_addr.s_addr = [self IPv4Pton:ip];
    _res.nscount = 1;
    
    unsigned char response[NS_PACKETSZ];
    
    
    //send mdns query
    if((len = res_9_query(QUERY_NAME, ns_c_in, ns_t_ptr, response, sizeof(response))) < 0) &#123;
        
        fprintf(stderr, "res_search(): %s\n", hstrerror(h_errno));
        return DUMMY_MAC_ADDR;
    &#125;//end if
    
    //parse mdns message
    ns_msg handle;
    if(ns_initparse(response, len, &handle) < 0) &#123;
        fprintf(stderr, "ns_initparse(): %s\n", hstrerror(h_errno));
        return DUMMY_MAC_ADDR;
    &#125;//end if
    
    //get answer length
    len = ns_msg_count(handle, ns_s_an);
    if(len < 0) &#123;
        fprintf(stderr, "ns_msg_count return zero\n");
        return DUMMY_MAC_ADDR;
    &#125;//end if
    
    //try to get mac address from data
    NSString *macAddress = nil;
    for(int i = 0 ; i < len ; i++) &#123;
        ns_rr rr;
        ns_parserr(&handle, ns_s_an, 0, &rr);
        
        if(ns_rr_class(rr) == ns_c_in &&
           ns_rr_type(rr) == ns_t_ptr &&
           !strcmp(ns_rr_name(rr), QUERY_NAME)) &#123;
            char *ptr = (char *)(ns_rr_rdata(rr) + 1);
            int l = (int)strcspn(ptr, "@");
            
            char *tmp = calloc(l + 1, sizeof(char));
            if(!tmp) &#123;
                perror("calloc()");
                continue;
            &#125;//end if
            memcpy(tmp, ptr, l);
            macAddress = [NSString stringWithUTF8String:tmp];
            free(tmp);
        &#125;//end if
    &#125;//end for each
    macAddress = macAddress ? macAddress : DUMMY_MAC_ADDR;
    return macAddress;
&#125;//end getMacAddressFromMDNS

- (nonnull NSString *)currentIPAddressOf: (nonnull NSString *)device &#123;
    struct ifaddrs *addrs;
    NSString *ipAddress = nil;
    
    if(getifaddrs(&addrs) != 0) &#123;
        return nil;
    &#125;//end if
    
    //get ipv4 address
    for(struct ifaddrs *addr = addrs ; addr ; addr = addr->ifa_next) &#123;
        if(!strcmp(addr->ifa_name, [device UTF8String])) &#123;
            if(addr->ifa_addr) &#123;
                struct sockaddr_in *in_addr = (struct sockaddr_in *)addr->ifa_addr;
                if(in_addr->sin_family == AF_INET) &#123;
                    ipAddress = [self IPv4Ntop:in_addr->sin_addr.s_addr];
                    break;
                &#125;//end if
            &#125;//end if
        &#125;//end if
    &#125;//end for
    
    freeifaddrs(addrs);
    return ipAddress;
&#125;//end currentIPAddressOf:

- (nullable NSString *)IPv4Ntop: (in_addr_t)addr &#123;
    char buffer[INET_ADDRSTRLEN] = &#123;0&#125;;
    return inet_ntop(AF_INET, &addr, buffer, sizeof(buffer)) ?
    [NSString stringWithUTF8String:buffer] : nil;
&#125;//end IPv4Ntop:

- (in_addr_t)IPv4Pton: (nonnull NSString *)IPAddr &#123;
    in_addr_t network = INADDR_NONE;
    return inet_pton(AF_INET, [IPAddr UTF8String], &network) == 1 ?
    network : INADDR_NONE;
&#125;//end IPv4Pton:
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果出现 “_res_9_ninit", referenced from:”这种报错，是因为没有添加步骤1的几个库</p>
</blockquote>
<h2 data-id="heading-4">3.UUID+自己存储</h2>
<h3 data-id="heading-5">3.1 获取UUID的两个方法</h3>
<pre><code class="hljs language-oc copyable" lang="oc">/**  卸载应用重新安装后会不一致*/
+ (NSString *)getUUID&#123;
    CFUUIDRef uuid = CFUUIDCreate(NULL);
    NSString *UUID = (__bridge_transfer NSString *)CFUUIDCreateString(NULL, uuid);
    CFRelease(uuid);
    return UUID;
&#125;
 
/**  卸载应用重新安装后会不一致*/
+ (NSString *)getUUID&#123;
    return [UIDevice currentDevice].identifierForVendor.UUIDString;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显UUID已经不足以支持设备的唯一性了，目前很多App都有新用户的优惠，但是又要保证每台设备绑定一个账户，如果单纯使用UUID的话已经满足不了这个需求，所以，这里需要用keychain保存，这样即使卸载app在安装，获取到的UUID也是唯一性的。</p>
<h3 data-id="heading-6">3.2 首先在项目中添加 KeyChain Sharing</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ffd17f0a11a428fbe14d13832dc3bef~tplv-k3u1fbpfcp-watermark.image" alt="WX20210422-152351.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">3.3 导入第三方库 Security.framework</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4369b8a8a07247c3a4d5a33f96fe0f89~tplv-k3u1fbpfcp-watermark.image" alt="1619076442209.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">3.4 核心代码（代码有点多）</h3>
<blockquote>
<p>在github搜索SSKeychain可以找到，只要 SSKeychain.h 和 SSKeychain.m 文件即可</p>
</blockquote>
<pre><code class="hljs language-oc copyable" lang="oc">#import <Foundation/Foundation.h>
#import <Security/Security.h>

/** Error codes that can be returned in NSError objects. */
typedef enum &#123;
/** No error. */
SSKeychainErrorNone = noErr,

/** Some of the arguments were invalid. */
SSKeychainErrorBadArguments = -1001,

/** There was no password. */
SSKeychainErrorNoPassword = -1002,

/** One or more parameters passed internally were not valid. */
SSKeychainErrorInvalidParameter = errSecParam,

/** Failed to allocate memory. */
SSKeychainErrorFailedToAllocated = errSecAllocate,

/** No trust results are available. */
SSKeychainErrorNotAvailable = errSecNotAvailable,

/** Authorization/Authentication failed. */
SSKeychainErrorAuthorizationFailed = errSecAuthFailed,

/** The item already exists. */
SSKeychainErrorDuplicatedItem = errSecDuplicateItem,

/** The item cannot be found.*/
SSKeychainErrorNotFound = errSecItemNotFound,

/** Interaction with the Security Server is not allowed. */
SSKeychainErrorInteractionNotAllowed = errSecInteractionNotAllowed,

/** Unable to decode the provided data. */
SSKeychainErrorFailedToDecode = errSecDecode
&#125; SSKeychainErrorCode;

extern NSString *const kSSKeychainErrorDomain;

/** Account name. */
extern NSString *const kSSKeychainAccountKey;

/**
 Time the item was created.
 
 The value will be a string.
 */
extern NSString *const kSSKeychainCreatedAtKey;

/** Item class. */
extern NSString *const kSSKeychainClassKey;

/** Item description. */
extern NSString *const kSSKeychainDescriptionKey;

/** Item label. */
extern NSString *const kSSKeychainLabelKey;

/** Time the item was last modified.
 
 The value will be a string.
 */
extern NSString *const kSSKeychainLastModifiedKey;

/** Where the item was created. */
extern NSString *const kSSKeychainWhereKey;

/**
 Simple wrapper for accessing accounts, getting passwords, setting passwords, and deleting passwords using the system
 Keychain on Mac OS X and iOS.
 
 This was originally inspired by EMKeychain and SDKeychain (both of which are now gone). Thanks to the authors.
 SSKeychain has since switched to a simpler implementation that was abstracted from [SSToolkit](http://sstoolk.it).
 */
@interface SSKeychain : NSObject

///-----------------------
/// @name Getting Accounts
///-----------------------

/**
 Returns an array containing the Keychain's accounts, or `nil` if the Keychain has no accounts.
 
 See the `NSString` constants declared in SSKeychain.h for a list of keys that can be used when accessing the
 dictionaries returned by this method.
 
 @return An array of dictionaries containing the Keychain's accounts, or `nil` if the Keychain doesn't have any
 accounts. The order of the objects in the array isn't defined.
 
 @see allAccounts:
 */
+ (NSArray *)allAccounts;

/**
 Returns an array containing the Keychain's accounts, or `nil` if the Keychain doesn't have any
 accounts.
 
 See the `NSString` constants declared in SSKeychain.h for a list of keys that can be used when accessing the
 dictionaries returned by this method.
 
 @param error If accessing the accounts fails, upon return contains an error that describes the problem.
 
 @return An array of dictionaries containing the Keychain's accounts, or `nil` if the Keychain doesn't have any
 accounts. The order of the objects in the array isn't defined.
  
 @see allAccounts
 */
+ (NSArray *)allAccounts:(NSError **)error;

/**
 Returns an array containing the Keychain's accounts for a given service, or `nil` if the Keychain doesn't have any
 accounts for the given service.
 
 See the `NSString` constants declared in SSKeychain.h for a list of keys that can be used when accessing the
 dictionaries returned by this method.
 
 @param serviceName The service for which to return the corresponding accounts.
 
 @return An array of dictionaries containing the Keychain's accountsfor a given `serviceName`, or `nil` if the Keychain
 doesn't have any accounts for the given `serviceName`. The order of the objects in the array isn't defined.
 
 @see accountsForService:error:
 */
+ (NSArray *)accountsForService:(NSString *)serviceName;

/**
 Returns an array containing the Keychain's accounts for a given service, or `nil` if the Keychain doesn't have any
 accounts for the given service.
 
 @param serviceName The service for which to return the corresponding accounts.
 
 @param error If accessing the accounts fails, upon return contains an error that describes the problem.
 
 @return An array of dictionaries containing the Keychain's accountsfor a given `serviceName`, or `nil` if the Keychain
 doesn't have any accounts for the given `serviceName`. The order of the objects in the array isn't defined.
 
 @see accountsForService:
 */
+ (NSArray *)accountsForService:(NSString *)serviceName error:(NSError **)error;


///------------------------
/// @name Getting Passwords
///------------------------

/**
 Returns a string containing the password for a given account and service, or `nil` if the Keychain doesn't have a
 password for the given parameters.
 
 @param serviceName The service for which to return the corresponding password.
 
 @param account The account for which to return the corresponding password.
 
 @return Returns a string containing the password for a given account and service, or `nil` if the Keychain doesn't
 have a password for the given parameters.
 
 @see passwordForService:account:error:
 */
+ (NSString *)passwordForService:(NSString *)serviceName account:(NSString *)account;

/**
 Returns a string containing the password for a given account and service, or `nil` if the Keychain doesn't have a
 password for the given parameters.
 
 @param serviceName The service for which to return the corresponding password.
 
 @param account The account for which to return the corresponding password.
 
 @param error If accessing the password fails, upon return contains an error that describes the problem.
 
 @return Returns a string containing the password for a given account and service, or `nil` if the Keychain doesn't
 have a password for the given parameters.
 
 @see passwordForService:account:
 */
+ (NSString *)passwordForService:(NSString *)serviceName account:(NSString *)account error:(NSError **)error;

/**
 Returns the password data for a given account and service, or `nil` if the Keychain doesn't have data 
 for the given parameters.
 
 @param serviceName The service for which to return the corresponding password.
 
 @param account The account for which to return the corresponding password.
 
 @param error If accessing the password fails, upon return contains an error that describes the problem.
 
 @return Returns a the password data for the given account and service, or `nil` if the Keychain doesn't
 have data for the given parameters.
 
 @see passwordDataForService:account:error:
 */
+ (NSData *)passwordDataForService:(NSString *)serviceName account:(NSString *)account;

/**
 Returns the password data for a given account and service, or `nil` if the Keychain doesn't have data 
 for the given parameters.
 
 @param serviceName The service for which to return the corresponding password.
 
 @param account The account for which to return the corresponding password.
 
 @param error If accessing the password fails, upon return contains an error that describes the problem.
 
 @return Returns a the password data for the given account and service, or `nil` if the Keychain doesn't
 have a password for the given parameters.
 
 @see passwordDataForService:account:
 */
+ (NSData *)passwordDataForService:(NSString *)serviceName account:(NSString *)account error:(NSError **)error;


///-------------------------
/// @name Deleting Passwords
///-------------------------

/**
 Deletes a password from the Keychain.
 
 @param serviceName The service for which to delete the corresponding password.
 
 @param account The account for which to delete the corresponding password.
 
 @return Returns `YES` on success, or `NO` on failure.
 
 @see deletePasswordForService:account:error:
 */
+ (BOOL)deletePasswordForService:(NSString *)serviceName account:(NSString *)account;

/**
 Deletes a password from the Keychain.
 
 @param serviceName The service for which to delete the corresponding password.
 
 @param account The account for which to delete the corresponding password.
 
 @param error If deleting the password fails, upon return contains an error that describes the problem.
 
 @return Returns `YES` on success, or `NO` on failure.
 
 @see deletePasswordForService:account:
 */
+ (BOOL)deletePasswordForService:(NSString *)serviceName account:(NSString *)account error:(NSError **)error;


///------------------------
/// @name Setting Passwords
///------------------------

/**
 Sets a password in the Keychain.
 
 @param password The password to store in the Keychain.
 
 @param serviceName The service for which to set the corresponding password.
 
 @param account The account for which to set the corresponding password.
 
 @return Returns `YES` on success, or `NO` on failure.
 
 @see setPassword:forService:account:error:
 */
+ (BOOL)setPassword:(NSString *)password forService:(NSString *)serviceName account:(NSString *)account;

/**
 Sets a password in the Keychain.
 
 @param password The password to store in the Keychain.
 
 @param serviceName The service for which to set the corresponding password.
 
 @param account The account for which to set the corresponding password.
 
 @param error If setting the password fails, upon return contains an error that describes the problem.
 
 @return Returns `YES` on success, or `NO` on failure.
 
 @see setPassword:forService:account:
 */
+ (BOOL)setPassword:(NSString *)password forService:(NSString *)serviceName account:(NSString *)account error:(NSError **)error;

/**
 Sets arbirary data in the Keychain.
 
 @param password The data to store in the Keychain.
 
 @param serviceName The service for which to set the corresponding password.
 
 @param account The account for which to set the corresponding password.
 
 @param error If setting the password fails, upon return contains an error that describes the problem.
 
 @return Returns `YES` on success, or `NO` on failure.
 
 @see setPasswordData:forService:account:error:
 */
+ (BOOL)setPasswordData:(NSData *)password forService:(NSString *)serviceName account:(NSString *)account;

/**
 Sets arbirary data in the Keychain.
 
 @param password The data to store in the Keychain.
 
 @param serviceName The service for which to set the corresponding password.
 
 @param account The account for which to set the corresponding password.
 
 @param error If setting the password fails, upon return contains an error that describes the problem.
 
 @return Returns `YES` on success, or `NO` on failure.
 
 @see setPasswordData:forService:account:
 */
+ (BOOL)setPasswordData:(NSData *)password forService:(NSString *)serviceName account:(NSString *)account error:(NSError **)error;


///--------------------
/// @name Configuration
///--------------------

#if __IPHONE_4_0 && TARGET_OS_IPHONE
/**
 Returns the accessibility type for all future passwords saved to the Keychain.
 
 @return Returns the accessibility type.
 
 The return value will be `NULL` or one of the "Keychain Item Accessibility Constants" used for determining when a
 keychain item should be readable.
 
 @see accessibilityType
 */
+ (CFTypeRef)accessibilityType;

/**
 Sets the accessibility type for all future passwords saved to the Keychain.
 
 @param accessibilityType One of the "Keychain Item Accessibility Constants" used for determining when a keychain item
 should be readable.
 
 If the value is `NULL` (the default), the Keychain default will be used.
 
 @see accessibilityType
 */
+ (void)setAccessibilityType:(CFTypeRef)accessibilityType;
#endif

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-oc copyable" lang="oc">#import "SSKeychain.h"

NSString *const kSSKeychainErrorDomain = @"com.samsoffes.sskeychain";

NSString *const kSSKeychainAccountKey = @"acct";
NSString *const kSSKeychainCreatedAtKey = @"cdat";
NSString *const kSSKeychainClassKey = @"labl";
NSString *const kSSKeychainDescriptionKey = @"desc";
NSString *const kSSKeychainLabelKey = @"labl";
NSString *const kSSKeychainLastModifiedKey = @"mdat";
NSString *const kSSKeychainWhereKey = @"svce";

#if __IPHONE_4_0 && TARGET_OS_IPHONE  
CFTypeRef SSKeychainAccessibilityType = NULL;
#endif

@interface SSKeychain ()
+ (NSMutableDictionary *)_queryForService:(NSString *)service account:(NSString *)account;
@end

@implementation SSKeychain

#pragma mark - Getting Accounts

+ (NSArray *)allAccounts &#123;
    return [self accountsForService:nil error:nil];
&#125;


+ (NSArray *)allAccounts:(NSError **)error &#123;
    return [self accountsForService:nil error:error];
&#125;


+ (NSArray *)accountsForService:(NSString *)service &#123;
    return [self accountsForService:service error:nil];
&#125;


+ (NSArray *)accountsForService:(NSString *)service error:(NSError **)error &#123;
    OSStatus status = SSKeychainErrorBadArguments;
    NSMutableDictionary *query = [self _queryForService:service account:nil];
#if __has_feature(objc_arc)
[query setObject:(__bridge id)kCFBooleanTrue forKey:(__bridge id)kSecReturnAttributes];
    [query setObject:(__bridge id)kSecMatchLimitAll forKey:(__bridge id)kSecMatchLimit];
#else
    [query setObject:(id)kCFBooleanTrue forKey:(id)kSecReturnAttributes];
    [query setObject:(id)kSecMatchLimitAll forKey:(id)kSecMatchLimit];
#endif

CFTypeRef result = NULL;
#if __has_feature(objc_arc)
    status = SecItemCopyMatching((__bridge CFDictionaryRef)query, &result);
#else
status = SecItemCopyMatching((CFDictionaryRef)query, &result);
#endif
    if (status != noErr && error != NULL) &#123;
*error = [NSError errorWithDomain:kSSKeychainErrorDomain code:status userInfo:nil];
return nil;
&#125;

#if __has_feature(objc_arc)
return (__bridge_transfer NSArray *)result;
#else
    return [(NSArray *)result autorelease];
#endif
&#125;


#pragma mark - Getting Passwords

+ (NSString *)passwordForService:(NSString *)service account:(NSString *)account &#123;
return [self passwordForService:service account:account error:nil];
&#125;


+ (NSString *)passwordForService:(NSString *)service account:(NSString *)account error:(NSError **)error &#123;
    NSData *data = [self passwordDataForService:service account:account error:error];
if (data.length > 0) &#123;
NSString *string = [[NSString alloc] initWithData:(NSData *)data encoding:NSUTF8StringEncoding];
#if !__has_feature(objc_arc)
[string autorelease];
#endif
return string;
&#125;

return nil;
&#125;


+ (NSData *)passwordDataForService:(NSString *)service account:(NSString *)account &#123;
    return [self passwordDataForService:service account:account error:nil];
&#125;


+ (NSData *)passwordDataForService:(NSString *)service account:(NSString *)account error:(NSError **)error &#123;
    OSStatus status = SSKeychainErrorBadArguments;
if (!service || !account) &#123;
if (error) &#123;
*error = [NSError errorWithDomain:kSSKeychainErrorDomain code:status userInfo:nil];
&#125;
return nil;
&#125;

CFTypeRef result = NULL;
NSMutableDictionary *query = [self _queryForService:service account:account];
#if __has_feature(objc_arc)
[query setObject:(__bridge id)kCFBooleanTrue forKey:(__bridge id)kSecReturnData];
[query setObject:(__bridge id)kSecMatchLimitOne forKey:(__bridge id)kSecMatchLimit];
status = SecItemCopyMatching((__bridge CFDictionaryRef)query, &result);
#else
[query setObject:(id)kCFBooleanTrue forKey:(id)kSecReturnData];
[query setObject:(id)kSecMatchLimitOne forKey:(id)kSecMatchLimit];
status = SecItemCopyMatching((CFDictionaryRef)query, &result);
#endif

if (status != noErr && error != NULL) &#123;
*error = [NSError errorWithDomain:kSSKeychainErrorDomain code:status userInfo:nil];
return nil;
&#125;

#if __has_feature(objc_arc)
return (__bridge_transfer NSData *)result;
#else
    return [(NSData *)result autorelease];
#endif
&#125;


#pragma mark - Deleting Passwords

+ (BOOL)deletePasswordForService:(NSString *)service account:(NSString *)account &#123;
return [self deletePasswordForService:service account:account error:nil];
&#125;


+ (BOOL)deletePasswordForService:(NSString *)service account:(NSString *)account error:(NSError **)error &#123;
OSStatus status = SSKeychainErrorBadArguments;
if (service && account) &#123;
NSMutableDictionary *query = [self _queryForService:service account:account];
#if __has_feature(objc_arc)
status = SecItemDelete((__bridge CFDictionaryRef)query);
#else
status = SecItemDelete((CFDictionaryRef)query);
#endif
&#125;
if (status != noErr && error != NULL) &#123;
*error = [NSError errorWithDomain:kSSKeychainErrorDomain code:status userInfo:nil];
&#125;
return (status == noErr);
    
&#125;


#pragma mark - Setting Passwords

+ (BOOL)setPassword:(NSString *)password forService:(NSString *)service account:(NSString *)account &#123;
return [self setPassword:password forService:service account:account error:nil];
&#125;


+ (BOOL)setPassword:(NSString *)password forService:(NSString *)service account:(NSString *)account error:(NSError **)error &#123;
    NSData *data = [password dataUsingEncoding:NSUTF8StringEncoding];
    return [self setPasswordData:data forService:service account:account error:error];
&#125;


+ (BOOL)setPasswordData:(NSData *)password forService:(NSString *)service account:(NSString *)account &#123;
    return [self setPasswordData:password forService:service account:account error:nil];
&#125;


+ (BOOL)setPasswordData:(NSData *)password forService:(NSString *)service account:(NSString *)account error:(NSError **)error &#123;
    OSStatus status = SSKeychainErrorBadArguments;
if (password && service && account) &#123;
        [self deletePasswordForService:service account:account];
        NSMutableDictionary *query = [self _queryForService:service account:account];
#if __has_feature(objc_arc)
[query setObject:password forKey:(__bridge id)kSecValueData];
#else
[query setObject:password forKey:(id)kSecValueData];
#endif

#if __IPHONE_4_0 && TARGET_OS_IPHONE
if (SSKeychainAccessibilityType) &#123;
#if __has_feature(objc_arc)
[query setObject:(id)[self accessibilityType] forKey:(__bridge id)kSecAttrAccessible];
#else
[query setObject:(id)[self accessibilityType] forKey:(id)kSecAttrAccessible];
#endif
&#125;
#endif

#if __has_feature(objc_arc)
        status = SecItemAdd((__bridge CFDictionaryRef)query, NULL);
#else
status = SecItemAdd((CFDictionaryRef)query, NULL);
#endif
&#125;
if (status != noErr && error != NULL) &#123;
*error = [NSError errorWithDomain:kSSKeychainErrorDomain code:status userInfo:nil];
&#125;
return (status == noErr);
&#125;


#pragma mark - Configuration

#if __IPHONE_4_0 && TARGET_OS_IPHONE 
+ (CFTypeRef)accessibilityType &#123;
return SSKeychainAccessibilityType;
&#125;


+ (void)setAccessibilityType:(CFTypeRef)accessibilityType &#123;
CFRetain(accessibilityType);
if (SSKeychainAccessibilityType) &#123;
CFRelease(SSKeychainAccessibilityType);
&#125;
SSKeychainAccessibilityType = accessibilityType;
&#125;
#endif


#pragma mark - Private

+ (NSMutableDictionary *)_queryForService:(NSString *)service account:(NSString *)account &#123;
    NSMutableDictionary *dictionary = [NSMutableDictionary dictionaryWithCapacity:3];
#if __has_feature(objc_arc)
    [dictionary setObject:(__bridge id)kSecClassGenericPassword forKey:(__bridge id)kSecClass];
#else
[dictionary setObject:(id)kSecClassGenericPassword forKey:(id)kSecClass];
#endif

    if (service) &#123;
#if __has_feature(objc_arc)
[dictionary setObject:service forKey:(__bridge id)kSecAttrService];
#else
[dictionary setObject:service forKey:(id)kSecAttrService];
#endif
&#125;

    if (account) &#123;
#if __has_feature(objc_arc)
[dictionary setObject:account forKey:(__bridge id)kSecAttrAccount];
#else
[dictionary setObject:account forKey:(id)kSecAttrAccount];
#endif
&#125;

    return dictionary;
&#125;

@end

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">3.4 创建新类，引用 SSKeychain 封装</h3>
<pre><code class="hljs language-oc copyable" lang="oc">#import "GetKeychain.h"
#import "SSKeychain.h"

@implementation GetKeychain

+ (NSString *)getDeviceUUID &#123;
    NSString *currentDeviceUUIDStr = [SSKeychain passwordForService:@"项目boudle id" account:@"uuid"];
    if (currentDeviceUUIDStr == nil || [currentDeviceUUIDStr isEqualToString:@""])
    &#123;
        NSUUID *currentDeviceUUID  = [UIDevice currentDevice].identifierForVendor;
        currentDeviceUUIDStr = currentDeviceUUID.UUIDString;
        currentDeviceUUIDStr = [currentDeviceUUIDStr stringByReplacingOccurrencesOfString:@"-" withString:@""];
        currentDeviceUUIDStr = [currentDeviceUUIDStr lowercaseString];
        [SSKeychain setPassword: currentDeviceUUIDStr forService:@"项目boudle id" account:@"uuid"];
    &#125;
    
    return currentDeviceUUIDStr;
&#125;

@end
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            