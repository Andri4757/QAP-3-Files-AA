
// Mo's Lawncare Services Invoice Calculator
// Author: Student
// Date: 2025-07-20

var $ = function (id) {
  return document.getElementById(id);
};

const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: 2,
  maximumFractionDigits: 2,
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: 2,
  maximumFractionDigits: 2,
});

function calculateInvoice() {
  // Get input values
  let name = $("custName").value;
  let address = $("custAddress").value;
  let city = $("custCity").value;
  let phone = $("custPhone").value;
  let sqft = parseFloat($("sqft").value);

  // Calculate service areas
  let borderSqft = sqft * 0.04;
  let mowingSqft = sqft * 0.95;
  let fertSqft = sqft;

  // Calculate service costs
  let borderCost = borderSqft * 0.35;
  let movingCost = mowingSqft * 0.07;
  let fertCost = fertSqft * 0.05;

  // Total charges before tax
  let totalCharges = borderCost + movingCost + fertCost;

  // Tax calculations
  let hst = totalCharges * 0.15;
  let envTax = totalCharges * 0.014;

  // Final total
  let invoiceTotal = totalCharges + hst + envTax;

  // Display customer block in 3 lines
  let customerBlock = name + "\n" + address + "\n" + city + " " + phone;
  $("custOutput").innerText = customerBlock;

  // Display calculations
  $("sqftOutput").innerText = com2Format.format(sqft);
  $("borderCost").innerText = cur2Format.format(borderCost);
  $("movingCost").innerText = cur2Format.format(movingCost);
  $("fertCost").innerText = cur2Format.format(fertCost);
  $("totalCharges").innerText = cur2Format.format(totalCharges);
  $("hst").innerText = cur2Format.format(hst);
  $("envTax").innerText = cur2Format.format(envTax);
  $("invoiceTotal").innerText = cur2Format.format(invoiceTotal);
}
