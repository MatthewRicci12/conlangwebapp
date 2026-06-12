  document.addEventListener('htmx:beforeRequest', function (evt) {
      if (evt.target.tagName === 'FORM') {
          window._pendingToast = true;
      }
  });

  document.addEventListener('htmx:afterSwap', function (evt) {
      if (window._pendingToast) {
          window._pendingToast = false;
          // Use setTimeout to let the new DOM fully settle
          setTimeout(function() {
              const toastEl = document.getElementById('liveToast');
              if (toastEl) {
                  const toast = new bootstrap.Toast(toastEl, { autohide: true, delay: 3000 });
                  toast.show();
              }
          }, 50);
      }
  });