// DOM元素
const searchInput = document.getElementById('searchInput');
const filterButtons = document.querySelectorAll('.filter-btn');
const serviceCards = document.querySelectorAll('.service-card');
const servicesGrid = document.getElementById('servicesGrid');
const emptyState = document.getElementById('emptyState');

// 当前过滤状态
let currentFilter = 'all';
let currentSearch = '';

// 初始化
document.addEventListener('DOMContentLoaded', function() {
    // 为搜索框添加事件监听器
    searchInput.addEventListener('input', handleSearch);
    
    // 为过滤按钮添加事件监听器
    filterButtons.forEach(button => {
        button.addEventListener('click', handleFilter);
    });

    // 为申请按钮添加事件监听器
    const applyButtons = document.querySelectorAll('.btn-primary');
    applyButtons.forEach(button => {
        button.addEventListener('click', handleServiceRequest);
    });

    // 添加加载动画
    animateCardsOnLoad();
});

// 搜索功能
function handleSearch(event) {
    currentSearch = event.target.value.toLowerCase().trim();
    filterServices();
}

// 过滤功能
function handleFilter(event) {
    // 移除所有按钮的活动状态
    filterButtons.forEach(btn => btn.classList.remove('active'));
    
    // 添加当前按钮的活动状态
    event.target.classList.add('active');
    
    // 更新当前过滤器
    currentFilter = event.target.getAttribute('data-category');
    
    // 应用过滤
    filterServices();
}

// 过滤服务卡片
function filterServices() {
    let visibleCount = 0;
    
    serviceCards.forEach(card => {
        const cardCategory = card.getAttribute('data-category');
        const cardTitle = card.querySelector('h3').textContent.toLowerCase();
        const cardDescription = card.querySelector('p').textContent.toLowerCase();
        
        // 检查分类过滤
        const categoryMatch = currentFilter === 'all' || cardCategory === currentFilter;
        
        // 检查搜索过滤
        const searchMatch = currentSearch === '' || 
                          cardTitle.includes(currentSearch) || 
                          cardDescription.includes(currentSearch);
        
        // 显示或隐藏卡片
        if (categoryMatch && searchMatch) {
            showCard(card);
            visibleCount++;
        } else {
            hideCard(card);
        }
    });
    
    // 显示或隐藏空状态
    if (visibleCount === 0) {
        emptyState.style.display = 'block';
        emptyState.style.animation = 'fadeInUp 0.5s ease-out';
    } else {
        emptyState.style.display = 'none';
    }
}

// 显示卡片
function showCard(card) {
    card.style.display = 'block';
    card.style.animation = 'fadeInUp 0.5s ease-out';
}

// 隐藏卡片
function hideCard(card) {
    card.style.animation = 'fadeOut 0.3s ease-out';
    setTimeout(() => {
        card.style.display = 'none';
    }, 300);
}

// 处理服务申请
function handleServiceRequest(event) {
    const card = event.target.closest('.service-card');
    const serviceName = card.querySelector('h3').textContent;
    
    // 添加加载状态
    const button = event.target;
    const originalText = button.textContent;
    button.textContent = '提交中...';
    button.disabled = true;
    
    // 模拟API调用
    setTimeout(() => {
        // 显示成功消息
        showNotification(`您的${serviceName}申请已提交成功！我们将在1个工作日内与您联系。`, 'success');
        
        // 恢复按钮状态
        button.textContent = originalText;
        button.disabled = false;
    }, 1500);
}

// 显示通知
function showNotification(message, type = 'info') {
    // 创建通知元素
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-info-circle'}"></i>
            <span>${message}</span>
            <button class="notification-close">×</button>
        </div>
    `;
    
    // 添加样式
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#4CAF50' : '#2196F3'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.2);
        z-index: 10000;
        max-width: 400px;
        animation: slideInRight 0.3s ease-out;
    `;
    
    // 添加到页面
    document.body.appendChild(notification);
    
    // 关闭按钮事件
    const closeBtn = notification.querySelector('.notification-close');
    closeBtn.addEventListener('click', () => {
        notification.style.animation = 'slideOutRight 0.3s ease-out';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    });
    
    // 自动关闭
    setTimeout(() => {
        if (document.body.contains(notification)) {
            notification.style.animation = 'slideOutRight 0.3s ease-out';
            setTimeout(() => {
                if (document.body.contains(notification)) {
                    document.body.removeChild(notification);
                }
            }, 300);
        }
    }, 5000);
}

// 页面加载时的动画
function animateCardsOnLoad() {
    serviceCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        
        setTimeout(() => {
            card.style.transition = 'all 0.6s ease-out';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
}

// 平滑滚动到顶部
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// 添加滚动到顶部按钮
window.addEventListener('scroll', function() {
    const scrollButton = document.getElementById('scrollTopBtn');
    if (!scrollButton) {
        // 创建滚动到顶部按钮
        const button = document.createElement('button');
        button.id = 'scrollTopBtn';
        button.innerHTML = '<i class="fas fa-chevron-up"></i>';
        button.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 50px;
            height: 50px;
            border: none;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            z-index: 1000;
            transition: all 0.3s ease;
            opacity: 0;
            transform: translateY(100px);
        `;
        button.addEventListener('click', scrollToTop);
        document.body.appendChild(button);
    }
    
    const scrollTopBtn = document.getElementById('scrollTopBtn');
    if (window.pageYOffset > 300) {
        scrollTopBtn.style.opacity = '1';
        scrollTopBtn.style.transform = 'translateY(0)';
    } else {
        scrollTopBtn.style.opacity = '0';
        scrollTopBtn.style.transform = 'translateY(100px)';
    }
});

// 键盘快捷键
document.addEventListener('keydown', function(event) {
    // Ctrl + K 或 Cmd + K 快速搜索
    if ((event.ctrlKey || event.metaKey) && event.key === 'k') {
        event.preventDefault();
        searchInput.focus();
        searchInput.select();
    }
    
    // ESC 清除搜索
    if (event.key === 'Escape') {
        searchInput.value = '';
        currentSearch = '';
        filterServices();
    }
});

// 添加搜索快捷键提示
searchInput.addEventListener('focus', function() {
    this.placeholder = '搜索服务... (ESC键清除)';
});

searchInput.addEventListener('blur', function() {
    this.placeholder = '搜索服务名称或描述...';
});

// 添加CSS动画
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
    
    @keyframes fadeOut {
        from {
            opacity: 1;
            transform: translateY(0);
        }
        to {
            opacity: 0;
            transform: translateY(-20px);
        }
    }
    
    .notification-content {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .notification-close {
        background: none;
        border: none;
        color: white;
        font-size: 1.2rem;
        cursor: pointer;
        margin-left: auto;
        padding: 0;
        width: 20px;
        height: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .notification-close:hover {
        opacity: 0.8;
    }
`;

document.head.appendChild(style);

// 统计和分析
let searchStats = {};
let filterStats = {};

// 记录搜索统计
function trackSearch(query) {
    if (query.length > 0) {
        searchStats[query] = (searchStats[query] || 0) + 1;
    }
}

// 记录过滤统计
function trackFilter(category) {
    filterStats[category] = (filterStats[category] || 0) + 1;
}

// 获取热门搜索
function getPopularSearches() {
    return Object.entries(searchStats)
        .sort(([,a], [,b]) => b - a)
        .slice(0, 5)
        .map(([query]) => query);
}

// 添加搜索建议
function addSearchSuggestions() {
    const suggestions = [
        '服务器', '数据库', '网络', '安全', '监控', '代码仓库', '环境配置'
    ];
    
    const datalist = document.createElement('datalist');
    datalist.id = 'searchSuggestions';
    
    suggestions.forEach(suggestion => {
        const option = document.createElement('option');
        option.value = suggestion;
        datalist.appendChild(option);
    });
    
    document.body.appendChild(datalist);
    searchInput.setAttribute('list', 'searchSuggestions');
}

// 初始化搜索建议
addSearchSuggestions();